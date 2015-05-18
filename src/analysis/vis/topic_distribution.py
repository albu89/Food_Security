'''
Created on May 18, 2015
@author: alexanderbusser
What does it do: Script to create image 3.8
Data Source: agg_vis.csv
'''
import csv
import plotly.plotly as py
from plotly.graph_objs import *



def vis_fil():
    tr_vis= csv.reader(open('/Users/alexanderbusser/Food_Security/time_series/ts_features/agg_vis.csv', 'rU'))
    tr1 = []; tr2 = []; tr3 = []; tr4 = []; x = []; 
    total = 0.0; poverty = 0.0; needs = 0.0; supply = 0.0; price = 0.0
    for rows in tr_vis:
        try:
            t = int(rows[1])
        except:
            continue
        
        total = int(rows[1]) + int(rows[2]) + int(rows[3]) + int(rows[4])
        poverty = 100 * float(rows[1])/total
        supply = (100 * float(rows[2])/total) + poverty
        needs = (100 * float(rows[3])/total) + supply
        price =  (100 * float(rows[4])/total) + needs
        
        print "poverty {} supply needs {} price {}".format(poverty, supply, needs, price)
           
        x.append(rows[0])
        tr1.append(poverty)
        tr2.append(supply)
        tr3.append(needs)
        tr4.append(price)
        total = 0 
    
    
    print tr1    
    trace1 = Scatter(
    x= x,
    y=tr1,
    fill='tozeroy'
)
    trace2 = Scatter(
    x= x,
    y=tr2,
    fill='tonexty'
)

    trace3 = Scatter(
    x= x,
    y=tr3,
    fill='tonexty'
)

    trace4 = Scatter(
    x= x,
    y=tr4,
    fill='tonexty'
)
    data = Data([trace1, trace2, trace3, trace4])
    plot_url = py.plot(data, filename='basic-area')
    


vis_fil()