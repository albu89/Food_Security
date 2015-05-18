'''
Created on May 17, 2015
@author: alexanderbusser
What does it do: Script to create image 3.9
Data Source: from annotations csv
'''

from __future__ import division
import plotly.plotly as py
from plotly.graph_objs import *



def create_vis():    
    trace1 = Bar(
        x= ["Supply", "Government", "Stability", "Economic Access" ],
        y= [4,1,2,1],
        name='Price_Conversation',
        visible=True
    )
    trace2 = Bar(
        x= ["Supply", "Government", "Stability", "Economic Access" ],
        y= [2,5,4,4],
        name='Poverty_Conversation'
    )
    
    trace3 = Bar(
        x= ["Supply", "Government", "Stability", "Economic Access" ],
        y= [2,0,1,1],
        name = 'Supply_Conversation'    
    )
     
    
    
    
    data = Data([trace1, trace2, trace3])
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




create_vis()