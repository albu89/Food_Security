 '''
@author: albu

'''


import csv, glob

path = "/home/alex/archive/food/new_archive/stats/*"

dest =  open("combined.csv", "a")  

for file in glob.glob(path):
	source1= open(file,"rb")
	for row in source1:
		dest.write(row)
