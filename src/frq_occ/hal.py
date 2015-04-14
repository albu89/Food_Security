'''
@author: Mike Gasser + albu
http://www.indiana.edu/~gasser/
'''
from nltk.corpus import brown
from nltk.corpus import stopwords
import math, operator
from nltk.metrics.paice import get_words_from_dictionary
from sample import extract_data


WINDOW = 8
FREQ_THRESH = 100
WORD_THRESH = 1000
STOP = set(stopwords.words('english'))
TEXT = ['its', 'the', 'end', 'of', 'the', 'glazed', 'donut', 'drought']
WORDS = ['its', 'the', 'end', 'of', 'glazed', 'donut', 'drought']


''' Mike Gasser '''
def indices(x, seq):
    '''List of indices in seq where x is found.'''
    return [pos for pos, item in enumerate(seq) if item == x]
''' Mike Gasser '''
def normalize(vector):
    '''Make the vector (really a list) length 1.0.
    Note: mutates the "vector"; return nothing.'''
    total = math.sqrt(sum([x**2 for x in vector]))
    for i in range(len(vector)):
        vector[i] /= total
''' Mike Gasser '''
def distance(vec1, vec2):
    '''Euclidian distance between the vectors.'''
    return math.sqrt(sum([(x - y)**2 for x,y in zip(vec1, vec2)]))
''' Mike Gasser '''
def cosine(vec1, vec2):
    '''Cosine similarity between two vectors (sequences).'''
    len1 = math.sqrt(sum([x**2 for x in vec1]))
    len2 = math.sqrt(sum([x**2 for x in vec2]))
    dot = sum([x*y for x,y in zip(vec1, vec2)])
    return dot / (len1 * len2)

''' Mike Gasser '''
def get_data():
    """Returns a text (list of words) and the list of the most frequent
    word types in the text."""
    print 'Getting text and frequent word types.'
    text = extract_data()
    tokens = text
    types = set(tokens)
    
    
    type_dict = dict([(t, 0) for t in types])
    i = 0
    n = len(types)
    print 'Found', n, 'types.'
    for tok in tokens:
        type_dict[tok] += 1
        i += 1
        if i % 100000 == 0:
            print 'Checked', i, 'tokens'
    freq_types = [t for t, f in type_dict.items() if f > FREQ_THRESH]
    print 'Found', len(freq_types), 'frequent word types.'
    return freq_types, text

''' Mike Gasser '''
class Memory(list):

    def __init__(self, words):
        self.n = len(words)
        self.positions = {}
        for index, word in enumerate(words):
            self.append(Word(word, index, self.n, self))

    def get_position(self, word):
        return self.positions.get(word, -1)

    def get_word(self, string):
        pos = self.get_position(string)
        if pos >= 0:
            return self[self.get_position(string)]

    def record(self, text):
        for pos in range(len(text)-1, -1, -1):
            if pos % 50000 == 0:
                print 'Recording at position', pos
            string = text[pos]
            word = self.get_word(string)
            if word:
                word.record_seg(pos-1, text, string)

    def make_meanings(self):
        for w in self:
            w.make_meaning()

    def compare(self, word1, word2):
        w1 = self.get_word(word1)
        w2 = self.get_word(word2)
        print w1
        if w1 and w2:
            return w1.distance(w2)

''' Mike Gasser '''
class Word(list):

    def __init__(self, string, index, length, memory):
        if index % 500 == 0:
            print 'Creating Word', index
        self.index = index
        self.string = string
        self.memory = memory
        self.meaning = []
        memory.positions[string] = index
        for i in range(length):
            self.append(0)

    def distance(self, word2):
        return cosine(self.meaning, word2.meaning)

    def record_seg(self, start, text, string):
        pos = start
        wt = WINDOW
        while pos >= 0 and wt >= 0:
            c_word = text[pos]
            if c_word != string:
                i = self.memory.get_position(c_word)
                if i >= 0:
                    self[i] += wt
            pos -= 1
            wt -= 1

    def make_meaning(self):
        self.meaning = self + self.get_column()

    def get_column(self):
        return [self.memory[i][self.index] for i in range(len(self.memory))]

words, text = get_data()
mem = Memory(words)
mem.record(text)
mem.make_meanings()
top_100 = {}

''' albu'''
while(True):
    x = raw_input("Enter word to compare with food such as available ;)")
    for item in words:
        sim = mem.compare(x, item)
        if len(top_100) > 500:
            min_key = min(top_100, key=top_100.get)
            del top_100[min_key]
            top_100[item] = sim
        else: 
            top_100[item] = sim 
    
    sorted_top_100 = sorted(top_100.items(), key=operator.itemgetter(1))        
    print sorted_top_100   
