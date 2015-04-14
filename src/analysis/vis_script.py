'''
Created on Mar 18, 2015

@author: albu
'''
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D 
import matplotlib as mpl
import math, csv
import numpy
from numpy import double

csv.field_size_limit(1000000000)




path = "/Users/alexanderbusser/Documents/thesis/data/" + "combined.csv"
tweets = pd.DataFrame()
df = pd.DataFrame()
test = pd.DataFrame()




tweets = pd.read_csv(path)


#print test
"""Country Plot"""

"""

countries =  tweets['country'].value_counts()
test = countries[countries > 100]
print test.index.values
countryIndex = test.index.values
numberCountry = test.values

data = {'occurence' : pd.Series(numberCountry, index=countryIndex) }
df = pd.DataFrame(data)



df.plot(kind='bar', title="Most popular Food-Tweeting countries")
    

plt.savefig('/Users/alexanderbusser/Documents/thesis/graphs/countryStats.png', bbox_inches='tight')




"""

"""Twitter User Ratio"""


df['tpu'] = tweets['user'].value_counts()
test['test'] = df['tpu'].value_counts()
test.to_csv('matlab.csv')




"""Food distribution  from https://datasciencelab.wordpress.com/2013/12/21/beautiful-plots-with-pandas-and-matplotlib/"""

"""


#print tweets['numTweets']

test = tweets['food'].value_counts()
#test.to_csv('foodDistribution.csv')

food =  test.index.values
numbersFood = test.values.astype(double)
print test

geoEnabled =  tweets['geo'].value_counts().values.astype(double)

percentage = numpy.divide((geoEnabled) , (numbersFood[:-1])) * 100


data = {'occurence' : pd.Series(numbersFood[:-1], index=food[:-1]), 'geo': pd.Series(percentage, index=food[:-1]) }
df = pd.DataFrame(data)

df = df.sort('geo')
fig, axes = plt.subplots(nrows=2, ncols=1)
for i, c in enumerate(df.columns):
    df[c].plot(kind='bar', ax=axes[i], figsize=(12, 10), title=c)
    

plt.savefig('/Users/alexanderbusser/Documents/thesis/graphs/food1.png', bbox_inches='tight')


# Create a figure of given size
fig = plt.figure(figsize=(16,12))
# Add a subplot
ax = fig.add_subplot(111)
# Set title
ttl = 'Number of Food related Tweets'

# Set color transparency (0: transparent; 1: solid)
a = 0.7
# Create a colormap
customcmap = [(x/40.0,  x/48.0, 0.05) for x in range(len(df))]


# Plot the 'population' column as horizontal bar plot
df['occurence'].plot(kind='barh', ax=ax, alpha=a,  legend=False, color=customcmap, edgecolor='w', xlim=(0,max(df['occurence'])), title=ttl)

plt.savefig('/Users/alexanderbusser/Documents/thesis/graphs/2.png', bbox_inches='tight')


# Remove grid lines (dotted lines inside plot)
ax.grid(False)
# Remove plot frame
ax.set_frame_on(False)
# Pandas trick: remove weird dotted line on axis
#ax.lines.set_visible(False)
ax.lines[0].set_visible(False)
 
# Customize title, set position, allow space on top of plot for title
ax.set_title(ax.get_title(), fontsize=26, alpha=a, ha='left')
plt.subplots_adjust(top=0.9)
ax.title.set_position((0,1.08))

 
# Position x tick labels on top
ax.xaxis.tick_top()
# Remove tick lines in x and y axes
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_ticks_position('none')
 
# Customize y tick labels
yticks = [item.get_text() for item in ax.get_yticklabels()]
ax.set_yticklabels(yticks, fontsize=16, alpha=a)
ax.yaxis.set_tick_params(pad=12)  

# Create a fake colorbar
ctb = LinearSegmentedColormap.from_list('custombar', customcmap, N=2048)
# Trick from http://stackoverflow.com/questions/8342549/
# matplotlib-add-colorbar-to-a-sequence-of-line-plots
sm = plt.cm.ScalarMappable(cmap=ctb, norm=plt.normalize(vmin=10, vmax=34))
# Fake up the array of the scalar mappable
sm._A = []
 
# Set colorbar, aspect ratio
cbar = plt.colorbar(sm, alpha=0.05, aspect=16, shrink=0.4)
cbar.solids.set_edgecolor("face")
# Remove colorbar container frame
cbar.outline.set_visible(False)
# Fontsize for colorbar ticklabels
cbar.ax.tick_params(labelsize=16)
# Customize colorbar tick labels

 
# Colorbar label, customize fontsize and distance to colorbar
cbar.set_label('Geo_Enabled in percentage', alpha=a, 
               rotation=270, fontsize=20, labelpad=50)
# Remove color bar tick lines, while keeping the tick labels
cbarytks = plt.getp(cbar.ax.axes, 'yticklines')
plt.setp(cbarytks, visible=False)


plt.savefig('/Users/alexanderbusser/Documents/thesis/graphs/numberFoodRelatedTweets.png', bbox_inches='tight')
"""

