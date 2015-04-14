'''

@author: alexanderbusser
'''


import bz2, json, profile, zipfile, time,unicodedata, tarfile, sys
from pprint import pprint
from food_categories import getFoodWordList, getFoodCatList


zipName = sys.argv[1]
outputName = sys.argv[2]

print zipName  + outputName

kwFood = ['meal','meals ', 'food','foods', 'wheat', 'rice', 'maize' 'carley', 'soybean', 'soy', 'meat' 
             'beef','cattle', 'chicken', 'poultry', 'lamb', 'swine', 'pork', 'fish', 'seafood', 'shrimp', 'salmon','sugar', 'bananas', 'oranges', 'coffee', 'cocoa', 'tea', 'milk'
            , 'yams', 'cassava', 'potatoes', 'sorghum', 'plantain', 'nuts', 'onion', 'salt', 'egg', 'dairy', 'cereals', 'SMP', 'WMP' ]


kwFactors = ['drought','flood', 'heat', 'wet', 'wettest','dry', 'extreme weather', 'monsoon', 'tornado', 'hurricane', 'storm', 'dollar', 'job', 'employment', 'unemployment'
             'oil', 'gasoline', 'kerosene', 'diesel', 'fuel', 'gas', 'biofuel', 'oils' ]



#kwFood = ['food']

#kwFactors = ['fuel']

termTime = 0



def matchFood(tweet):

    nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
    nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
    tweet = nTweet.lower().split()

        
    for l in getFoodWordList():
        if l in tweet:
            return True
                    
    
    return False

def matchFactor(tweet):

    nTweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
    nTweet = nTweet.translate(None, '\"\'.,;?!:)(@/*&)')
    tweet = nTweet.lower().split()

        
    for l in kwFactors:
        if l in tweet:
            return True
                    
    
    return False


def load_bz2_json(data):
    """ Takes a bz2 filename, returns the tweets as a list of tweet dictionaries"""
    
   
    lines = bz2.decompress(data).split("\n")
    num_lines = len(lines)
    tweets = []
    for line in lines:
        try:
            if line == "":
                num_lines -= 1
                continue
            tweets.append(json.loads(line))
        except: 
            print "Decoding error"
            continue
    return tweets


def handle_file(filename):
    tweets = load_bz2_json(filename)
      
    for tweet in tweets:
        try:
            if matchFood(tweet['text']):
                
                with open("new_food/food"+outputName+".json", 'a+') as outfile:
                    json.dump(tweet, outfile)
                    outfile.write('\n')
        except:
            continue
    
    return True



def main():
    
    start = time.time()
    #path = "/Users/alexanderbusser/Documents/thesis/data/tweets" + zipName
    path = "/home/alex/archive/tweets" + zipName 
    files_processed = 0
       
    
    if "zip" in zipName:   
        try: 
            print path
            zip = zipfile.ZipFile(path) 
            nameList = zip.namelist()
            type = "zip"
        
        except:
            print "Zip-file could not be opened"
           
     
    if "tar" in zipName:
        try:
            print zipName
            tar = tarfile.open(path)
            nameList = tar.getnames()
            type = "tar"
             
        except: 
            print "Tar-file could not be opened"
        
    for info in nameList:
        #filename = info.filename
        try:
            if "json.bz2"  in info and "._" not in info:
                if type == "zip":
                    data = zip.read(info)
                else:
                    print info
                    
                    test = tar.extractfile(info)
                    data = test.read()
                    #print data
                files_processed +=1
                print('Starting work on file ' + str(files_processed) + '): ' + info)
                handle_file(data)    
    
        except KeyError:
            print 'KeyError'
                        
    end = time.time() - start
    print "Filtering time %s " %end

if __name__ == "__main__":
    pprint('Starting work!')
    
    profile.run('main()')
   
else:  # If running interactively in interpreter (Pycharm):
    filename = r"H:\Twitter datastream\PYTHONCACHE\2013\01\01\00\00.json.bz2"