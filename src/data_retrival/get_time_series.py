'''
Created on May 13, 2015
@author: alexanderbusser
What does it do: Creates Time Series daily/weekly and removes holidays
Data Source: From data/raw  on github
'''
from calendar import month
import csv, collections
import src.food_categories as fc
from datetime import datetime
import pandas as pd
from collections import OrderedDict
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

allCat = ['general', 'meat', 'dairy', 'cereals', 'oil_vegetable', 'sugar']

"""Categorise by category e.g. Meat or subcategory e.g. Beef """
category = False
"""Create Count of all """
computeAll = False


""" Input Category name get aggregated Values"""   

def aggregate(name):
    
    f_time = collections.OrderedDict()
    cat_val = []; a_dates = []; a_values = []
    data = read_csv()
    if category:
        cat_val = fc.get_food_words()[name]
    else:
        if computeAll:
            for element in allCat:
                cat_val.extend(fc.get_food_words()[element])
        else:
            cat_val.append(name)
   

            
    for rows in data:
        for item in cat_val:
         
            if rows[1] in item:
                try:
                    volume = int(rows[2])
                except:
                    continue
                
                if (rows[0], name) in f_time:
                    f_time[(rows[0], name)]+=volume
                else: 
                    f_time[(rows[0],name)] = volume
                    
    print "Agregate done"
    
    description = True
    
    reindex = {}
    for k, v in f_time.items(): 
        time, food = k
        time = datetime.strptime(time, "%d/%m/%y").strftime("%m/%d/%y");
        print time
        count = v
        reindex[time] = count
    bday_us = CustomBusinessDay(calendar=USFederalHolidayCalendar())
 
    idx = pd.date_range('01/02/2012', '09/26/2014', freq=bday_us)
    idx = idx[idx.dayofweek<5]
    s = pd.Series(reindex)
    s.index = pd.DatetimeIndex(s.index)
    s = s.reindex(idx, fill_value=0)
    
    
    s = s.resample('M', how='mean')
    
    f_time = collections.OrderedDict()
   
    f_time = s.to_dict()
    reindex = {}
    for k,v in f_time.items():
        time = k.strftime("%Y-%m-%d %H:%M:%S") 
        count = v
        reindex[time] = count
    
    ordered = OrderedDict(sorted(reindex.items(), key=lambda t: t[0]))
  
    
    for k,v in ordered.items():
        time = k
        count = v
        csv_writer(description, name, time, count)
        a_values.append(count)
        a_dates.append(time)
        description = False
                
    return a_dates, a_values

""" Read Raw CSV """
def read_csv():
    reader = csv.reader(open('/Users/alexanderbusser/Food_Security/data/raw/m_supply.csv', 'rU'))
    return reader

""" Write TS to File """        
def csv_writer(description, name, time, count):
    f = open('/Users/alexanderbusser/Food_Security/time_series/'+name+'.csv', 'a')
    writer = csv.writer(f)
    if description:
        writer.writerow(('date', name))    
    try:
        row = (time, count)
        values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
        writer.writerow(values)
        
    except KeyError:
        return True   
            

""" Helper method to create TS of all products """

def iterate_commodities (name):            
    cat_val = fc.get_food_words()[name]
    to_file = []
    for item in cat_val:
        a_date, a_values = aggregate(item)

 
 
"""Enter commodity name such as port to create """  
aggregate('pork')


