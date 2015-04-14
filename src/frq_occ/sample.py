'''
@author: alexanderbusser
'''

import glob, random, json, os, math, re
from nltk.corpus import stopwords
from random import randint




count = 0
stop = stopwords.words('english')

#path = "/Users/alexanderbusser/Documents/thesis/data/order"
path = "/home/alex/archive/food/new_archive"

value = True
def data_list():
    nFileList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if "json" in file:
                print(os.path.join(root, file))
                nFile = os.path.join(root, file)
                nFileList.append(nFile)
                 
     
    return nFileList            
                 
                 
""" Create Corpus from Sample 20 %"""     
           
def extract_data():
    prev_value = []
    corpus = []
    value = True
    source = data_list()
    total_words = 0
    print len(source)
    length = len(source)
    percent = int(math.ceil(length * 0.1))
    print percent
    for x in range(0, percent):
        while(value):
            index = randint(0,length-1)
            if index not in prev_value:
                value = False
                prev_value.append(index)
        
	name = source[randint(0,length-1)]
        print name
        tweets= open(name,"rb")
         
        for tweet in tweets:
                try:
                    if tweet == "":
                        continue
        
                    text = json.loads(tweet)['text'].lower()
                    words = re.findall(r'\w+', text,flags = re.UNICODE | re.LOCALE) 
                    line = [i for i in words if i not in stop]
		    total_words = total_words + len(line)
                    corpus.extend(line)
                except: 
                    print "Decoding error"
                    continue

    print "print total words: {}".format(total_words)
    
    try:         
        with open("/home/alex/archive/food/testSample.json", 'a+') as outfile:
            for words in corpus:
                json.dump(words, outfile)
                outfile.write('\n')
    except:
        print "error"

    return corpus

def top_k(word_list):
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    
    return word_counter           

def main():
   
    corpus = extract_data()
    while(True):
        x = raw_input('1 for top 500 2 for HAL?')
        if "1" in x:
            word_count = top_k(corpus)
            popular_words = sorted(word_count, key = word_count.get, reverse = True)
            top_3 = popular_words[:500]
            print top_3
            f = open('myfile','w')
            for item in top_3:
                f.write(item + '\n')
            
            
            f.close() 
                
          

if __name__ == "__main__":
    main()


