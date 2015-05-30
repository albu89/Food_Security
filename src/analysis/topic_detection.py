'''
Created on May 17, 2015
@author: alexanderbusser
What does it do: Script to explore content of tweets
Data Source: data/fsec_tweets
'''


import os, json, sys, re
from nltk.corpus import stopwords
from collections import Counter
stop = stopwords.words('english')
from itertools import islice, izip


"""Specify destination of output"""
orig_stdout = sys.stdout
f = file('/Users/alexanderbusser/Food_Security/time_series/ts_features/test/topic_detect.txt', 'w')
sys.stdout = f


"""Return top k words"""
def top_k(word_list):
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    
    return word_counter  
    
    
"""Read Json"""
def read_json(): 
    corpus = []
    n_name = ""
    exten = ".json"

    path = '/Users/alexanderbusser/Food_Security/time_series/ts_features/test/test/t_needs'
    for path, subdirs, files in os.walk(path):
        for name in files:
            if exten in name.lower():
                n_name = (os.path.join(path, name))
                tweets_data = []
                tweets_file = open(n_name, "r")
                for line in tweets_file:
                    try:
                            tweet = json.loads(line)
                            if "2014" in tweet['created_at'] and "Aug 11" in tweet['created_at'] : 
                                
                                text = tweet['text'].lower()
                                print text
                                
                                words = re.findall(r'\w+', text,flags = re.UNICODE | re.LOCALE) 
                                line = [i for i in words if i not in stop]
                           
                                corpus.extend(line)  
                                
                    except:
                            continue
    
    return corpus
            


def main():
    
    corpus = read_json() 
    
    word_count = top_k(corpus)
    popular_words = sorted(word_count, key = word_count.get, reverse = True)
    top_50 = popular_words[:50]
    print top_50

    
    lString = ' '.join(corpus)
    words = re.findall("\w+", lString)
    print Counter(izip(words, islice(words, 1, None))).most_common(10)
    


"""Execute script"""
main()
            
        
                
