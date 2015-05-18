'''
Created on Apr 16, 2015

@author: alexanderbusser
What does it do: Script to create image 3.2 b)
Data Source: m_all.csv


'''

from __future__ import division

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D 
import csv
from numpy import double
import plotly.plotly as py
from plotly.graph_objs import *
from src import food_categories as fc
csv.field_size_limit(1000000000)
py.sign_in('alexander.buesser', 'g51hbbu2ag')






def ret_count(item):
    data = csv.reader(open('/Users/alexanderbusser/Food_Security/time_series/ts_features/raw/m_all.csv', 'rU'))   
    totalVal = 0
    for rows in data:
        
        if rows[1] == item:
            try: 
                totalVal = totalVal + int(rows[2])
                
            except:
                continue
    #print totalVal
    return totalVal





order_top_cat = ['meat', 'dairy', 'cereals', 'oil', 'sugar', 'others' ]
order_top_name = ['meat', 'dairy', 'cereals', 'vegetable oil', 'sugar', 'others' ]
val = 0
bar_val = []
for element in order_top_cat:
    val = 0 
    cat_element = fc.get_food_words()[element]
    for item in cat_element:
        try:
            val+=ret_count(item)
        except: 
            print "error {}".format(item)
    bar_val.append(val)

print bar_val

total_ini = 0
total_inc = 0
for el in bar_val:
    total_ini = total_ini + el

p_meat = bar_val[0]/total_ini
p_dairy = bar_val[1]/total_ini
p_cereals = bar_val[2]/total_ini
p_oil = bar_val[3]/total_ini
p_sugar = bar_val[4]/total_ini
p_oher = bar_val[5]/total_ini

print "meat {} dairy {} cereals {} oil {} sugar {} other {}".format(p_meat, p_dairy, p_cereals, p_oil, p_sugar, p_oher)


trace1 = Bar(
    x= order_top_name,
    y= bar_val,
    name='Volume Category',
    visible=True
)


data = Data([trace1])
layout = Layout(
    title='Category Distribution',
    showlegend=True,
    autosize=True,
    width=725,
    height=521,
    xaxis=XAxis(
        title='Category',
       
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

py.plot(fig, filename= 'cat_distribution')