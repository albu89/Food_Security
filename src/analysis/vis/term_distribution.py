'''
Created on Apr 16, 2015
@author: alexanderbusser
What does it do: Script to create image 3.2 a)
Data Source: m_all.csv
'''
from __future__ import division
import  csv
import plotly.plotly as py
from plotly.graph_objs import *
import sys
sys.path.insert(1,'/path/to/mod_directory')
from src import food_categories as fc

csv.field_size_limit(1000000000)
py.sign_in('alexander.buesser', 'g51hbbu2ag')



order_cat = ['pork', 'chicken','lamb', 'beef', 'milk','egg','rice','corn','wheat',
             'tea','fish','oil_soy','sugar','coffee', 'potato', 'coca','salt', 'general']
name_cat = ['pork', 'chicken','lamb', 'beef','milk','egg', 'rice','corn','wheat', 'tea',
            'fish','soya','sugar','coffee', 'potato', 'coca','salt', 'general']



"""Get Count value of certain product"""
def ret_count(item):
    data = csv.reader(open('/Users/alexanderbusser/Food_Security/time_series/ts_features/raw/m_all.csv', 'rU'))   
    totalVal = 0
    for rows in data:
        
        if rows[1] == item:
            try: 
                totalVal = totalVal + int(rows[2])
                
            except:
                continue

    return totalVal

""" Create Image """
def create_img():
    bar_ini = []; bar_inc = []; total_ini = 0; total_inc = 0


    for element in order_cat:
        ini_Val = 0
        inc_Val= 0
        cat_element = fc.get_food_words()[element]
        if element == "general": 
            ini_Val = ret_count('food') + ret_count('foods') + ret_count('meal') + ret_count('meals')
            inc_Val = ret_count('breakfast')+ ret_count('lunch')+ret_count('dinner')
            bar_ini.append(ini_Val)
            bar_inc.append(inc_Val)
            continue
             
        
        for item in cat_element:
           
            if element == item:
                try:
                    ini_Val = ret_count(item)
                except:
                    print "error {}".format(item)
            else:
                try:
                
                    inc_Val+=ret_count(item)
                except: 
                    print "error {}".format(item)
                
        bar_ini.append(ini_Val)
        bar_inc.append(inc_Val)
        
    print  bar_ini
    
    for el in bar_ini:
        total_ini = total_ini + el
    
    for el in bar_inc:
        total_inc = total_inc + el
        
    print "Total number ini {} total number aded {}".format(total_ini, total_inc)
    
    trace1 = Bar(
        x= order_cat,
        y= bar_ini,
        name='Volume initial Keywords ',
        visible=True
    )
    trace2 = Bar(
        x= order_cat,
        y= bar_inc,
        name='Added Volume'
    )
    
    data = Data([trace1, trace2])
    layout = Layout(
        title='Number of Food related Tweets',
        showlegend=True,
        autosize=True,
        width=725,
        height=521,
        xaxis=XAxis(
            title='Food Term',
           
        ),
        yaxis=YAxis(
            title='Twitter Volume',
            range=[0, 458912.63157894736],
            type='linear',
            autorange=True,
            exponentformat='SI',
            showexponent='last'
        ),
        legend=Legend(
            x=1.0204520990312163,
            y=0.009685230024213076
        ),
        barmode='stack'
    )
    fig = Figure(data=data, layout=layout)
    
    py.plot(fig)



create_img()
