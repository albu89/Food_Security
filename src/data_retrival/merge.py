'''
@author: albu
'''

import glob
import pandas as pd


path ="/home/alex/archive/food/new_archive/stats/*"
#path = "/Users/alexanderbusser/Documents/thesis/miningCommodities/twitter/src/textMining/csv/*"


frame = pd.DataFrame()
list = []



for file in glob.glob(path):
    try:
        df = pd.read_csv(file,index_col=0)
        list.append(df)
    except:
        continue
    

frame = pd.concat(list)

frame.to_csv('new_archive/stats/summary.csv')

