'''
Created on Mar 17, 2015

@author: albu
'''

import bz2, json, profile, zipfile, time,unicodedata, tarfile, sys, csv
from pprint import pprint

import json
import pandas as pd


sourceName = sys.argv[1]
outputNumber = sys.argv[2]

#path = "/Users/alexanderbusser/Documents/thesis/data/" + sourceName
path = sourceName 

kwFood = ['meal','meals','food','foods','wheat', 'rice', 'maize','carley', 'soybean', 'soy', 'meat', 
             'beef','cattle', 'chicken', 'poultry', 'lamb', 'swine', 'pork', 'fish', 'seafood', 'shrimp', 'salmon','sugar', 'bananas', 'oranges', 'coffee', 'cocoa', 'tea', 'milk'
            , 'yams', 'cassava', 'potatoes', 'sorghum', 'plantain', 'nuts', 'onion', 'salt', 'egg', 'dairy', 'cereals', 'SMP', 'WMP' ]


tweets = pd.DataFrame()

def matchFood(tweet):
        nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
        nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
        tweet= nTweet.lower().split()

        
        for l in kwFood:
            if l in tweet:
               
                return l
                    
    
        return ""
    
    
def matchUser(tweet, user):
        nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
        nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
        tweet= nTweet.lower().split()

        
        for l in kwFood:
            if l in tweet:
               
                return user
                    
    
        return ""

def matchGeo(tweet, geo):
        nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
        nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
        tweet= nTweet.lower().split()

        for l in kwFood:
            if l in tweet and geo:
                return l
        return ""




tweets_data = []
tweets_file = open(path, "r")

for line in tweets_file:
    try:
	tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
    

    

tweets['lang'] = map(lambda tweet: tweet['user']['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets['numTweets'] = None
tweets['numTweets'][0] = len(tweets_data)
tweets['food']= map(lambda tweet:matchFood(tweet['text'] ), tweets_data )    

tweets['user']= map(lambda tweet:matchUser(tweet['text'], tweet['user']['id']), tweets_data )
tweets['geo']= map(lambda tweet:matchGeo  (tweet['text'], tweet['user']['geo_enabled']), tweets_data )  


status = True;

while(status):
    try:
        print path
	tweets.to_csv("new_archive/stats/foodStats" + outputNumber +".csv")
        status = False;
    except:
	status = False
	print path
