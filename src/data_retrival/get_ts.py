'''
Created on May 18, 2015

@author: alexanderbusser
'''


import json,sys,os, unicodedata,csv, glob
from pytz import timezone
from src import food_categories as fc
from datetime import datetime


filename = sys.argv[1]
number  = sys.argv[2]

path = "/home/alex/archive/food/predictor_tweets/test/ts_price/" + filename



"""Exact Strig matching"""
def matchFood(tweet):
        nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
        nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
        tweet= nTweet.lower().split()
        
        for l in fc.getFoodWordList():
            if l in tweet:
                return l
          
    
        return ""


  
"""Read Json"""
def json_read(filename):
    tweets_data = []
    tweets_file = open(filename, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
    
    return tweets_data

"""Write to CSV"""
def csv_writer(tweets,count):
    path = '/home/alex/archive/time_series_predictor/ts_all/food_{}_{}.csv'.format(number,count)
    f = open(path, 'a')
    writer = csv.writer(f)
    writer.writerow( ('date', 'food', 'count') )
    ts_food = {}
    for tweet in tweets:
        time, food = strip_tweet(tweet)  
        if food == "":
            continue
        
        if (time,food) in ts_food:
            ts_food[(time,food)]+=1
        else: 
            ts_food[(time,food)] = 1
    
    for k,v in ts_food.items():
        time,food = k
        count = v
        try:
            row = (time,food, count)
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row] 
            writer.writerow(values)
        
        except KeyError:
            print "Error"
            return True
    


""" Get Date and Food """
def strip_tweet(tweet):
    utc = timezone('UTC')
    created_at = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    d = utc.localize(created_at)
    time =  d.strftime("%d/%m/%y") 
    food = matchFood(tweet['text'] )
    return time, food


def main ():
    exten = ".json"
    count = 0
    for path, subdirs, files in os.walk(filename):
            for name in files:
                    if exten in name.lower():
                            n_name = (os.path.join(path, name))
                            print "Start {}".format(n_name)
                            data = json_read(n_name)
                            csv_writer(data,count)
                            print "Done {}".format(n_name)
    


main() 
