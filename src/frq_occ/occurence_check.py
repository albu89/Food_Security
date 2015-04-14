'''
Created on Mar 26, 2015

This script returns the 30 most occuring Nouns


@author: alexanderbusser
'''

import nltk, json, sys, os

from nltk.corpus import brown
from nltk.corpus import treebank
import nltk.tag
from nltk import pos_tag

path = sys.argv[0]
      
def process_tweets(tweets):
    a = []
    for tweet in tweets:
        tokens = nltk.word_tokenize(tweet['text'])
        tagged = nltk.pos_tag(tokens)
        
        for item in tagged:
            if item[1][0] == 'N' or item[1][0] == 'J':
                a.append(item[0])
    
    
    word_count = top_k(a)
    popular_words = sorted(word_count, key = word_count.get, reverse = True)
    top_3 = popular_words[:500]
    
    print top_3
    
          

def top_k(word_list):
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    
    return word_counter       
      

def main():
    
    tweets_data = []
    path = '/Users/alexanderbusser/Documents/thesis/data/foodSec/supply_low/'
    
    for i in os.listdir('/Users/alexanderbusser/Documents/thesis/data/foodSec/supply_low'):
        
        tweets_file = open(path+i, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue
      
        process_tweets(tweets_data)
        
    
if __name__ == "__main__":
    main()