'''
@author: albu + humanitas
'''


import get_category,re, json,csv, sys
from food_categories import getFoodWordList, getFoodCatList


readFile = sys.argv[1]
outputNumber = sys.argv[2]


''' albu '''

def compress (tweet):
    data = {}
    data['text'] = tweet['text']
    data['user_id'] = tweet['user']['id']
    data['user_geo_enabled'] = tweet['user']['geo_enabled']
    data['user_location'] = tweet['user']['location']
    if tweet['place'] != None:
        data['place_country']= tweet['place']['country']
          
    else:
        data['place_country']= None
        
         
    data['user_lang'] = tweet['user']['lang']
     
    if tweet['geo'] != None:
        data['geo_coordinates'] =  tweet['geo']['coordinates']
    else:
        data['geo_coordinates'] = None
           
    data['created_at'] = tweet['created_at']   
    
    return data
    
''' humanitas '''
def get_tokens(tweet):
        tweet_text_lower = tweet['text'].lower().encode("ascii","ignore")
        tweet_text_clean = re.sub('[^a-zA-Z0-9-]', ' ', tweet_text_lower)
        tweet_text_tokens = tweet_text_clean.split()
        return tweet_text_tokens


''' albu '''
def json_writer(outputName, tweet):
    c_tweet = compress(tweet)
    with open("/home/alex/archive/food/lexicon/" + outputName + ".json", 'a+') as outfile:
                    json.dump(c_tweet, outfile)
                    outfile.write('\n')


''' humanitas '''

def containsWord(tweet_tokens):
    food_word_dict = getFoodWordList()
    for e in tweet_tokens:
        if e in food_word_dict:
            return e
    return ''

''' albu '''
def process_tweets(tweet_set):
        
        inserts = { }    
        for tweet in tweet_set:
            tweet_tokens = get_tokens(tweet)
            food = containsWord(tweet_tokens) 
            if food != '':
                name = extract_features(tweet, tweet_tokens)
                if name != '': 
                    index = food + "_" + name
                    inserts[index] = inserts.get(index, 0)  + 1
                    json_writer(name, tweet)
                    
                   
        
        
        writer = csv.writer(open('/home/alex/archive/food/stats/dict'+outputNumber+'.csv', 'wb'))
        for key, value in inserts.items():
            writer.writerow([key, value])
        
                
                 
''' humanitas '''
def extract_features(t, tokens):
        category_count = {}
        cat_n = ""
        prev_neg = False
        # Position in tweet
        pos = -1
        last_negation_pos = -1
        max_neg_distance = 2
      
        for token in tokens:
            pos += 1
            #stemming is done here
            cat = get_category.get_category(token)
           
            if not cat: continue
        
            if cat[0] in 'negation':
                # Negation
                prev_neg = True
                last_negation_pos = pos
                
            elif cat[1] is not None:
                # Ordinary word
                cat_n = '_'.join(c for c in cat)
                if prev_neg:
                    prev_neg = False
                    if pos - last_negation_pos <= max_neg_distance:
                        compl_cat = get_category.compl_pred_cats[cat[1]]
                        cat_n = '_'.join([cat[0],compl_cat])
                        
                if cat_n in category_count:
                    category_count[cat_n] += 1
                else:
                    category_count[cat_n] = 1

        counts = sum(category_count.values())
        #category_count['cnts'] = counts
        
        
        return cat_n
    
    
 ''' albu + humanitas '''   
def main():

    path = readFile
    print path
    
    get_category.init_reverse_index()
    food_categories = getFoodCatList()
    pred_categories = get_category.pred_categories
    get_category.extend_categories(food_categories)
    get_category.extend_categories(['cnts'])
    print get_category.c_stems
    print get_category.compl_pred_cats
    print get_category.additional_categories
    print getFoodWordList()
    
    tweets_data = []
    tweets_file = open(path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
        
    process_tweets( tweets_data)

if __name__ == "__main__":
    main()