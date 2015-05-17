'''
Created on May 13, 2015

@author: alexanderbusser
'''
import json,os,csv


""" Json extraction""" 

def count_user_id():
    exten = ".json"
    f = open('/home/alex/archive/user_count.csv', 'a')
    writer = csv.writer(f)
    writer.writerow( ('UserID', 'count') )

    for path, subdirs, files in os.walk('/home/alex/archive/new_food/'):
        for name in files:
            if exten in name.lower():
                n_name = (os.path.join(path, name))
                print n_name
    
                user_id_dic = {} 
                tweets_data = []
                tweets_file = open(n_name, "r")
                for line in tweets_file:
                    try:
                        tweet = json.loads(line)
                        user_id = tweet['user']['id']
                        
                        if user_id in user_id_dic:
                            user_id_dic[user_id]+=1
                        else: 
                            user_id_dic[user_id] = 1
            
                        tweets_data.append(tweet)
                    except: 
                        continue
     
    print "write final file"
    
    for k,v in user_id_dic.items():
        userID = k
        count = v
        try:
            row = (userID, count)
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            writer.writerow(values)
        
        except KeyError:
            return True               


"""perform aggregation of values"""

def post_processing ():
    f = open('/Users/alexanderbusser/Food_Security/data/new_user_count.csv', 'a')
    writer = csv.writer(f)
    writer.writerow( ('Number of Tweets', 'Number of Users') )
    reader = csv.reader(open('/Users/alexanderbusser/Food_Security/data/user_count.csv', 'rU'))
    user_id_dic = {}
    count = 0
    for rows in reader:
        count +=1
        if rows[1] in user_id_dic:
            user_id_dic[rows[1]]+=1
        else: 
            user_id_dic[rows[1]] = 1
    
    print "write final file"
    print count
    
    for k,v in user_id_dic.items():
        userID = k
        count = v
        try:
            row = (userID, count)
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            writer.writerow(values)
        
        except KeyError:
            return True           
    

""" Start extraction from json """
count_user_id()


""" Uncomment for post_processing """
#post_processing()