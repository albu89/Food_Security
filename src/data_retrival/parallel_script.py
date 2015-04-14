'''
@author: albu
'''

import os, sys, glob


#text_file = open("pathStats.txt", "r")

#lines = text_file.readlines()
cpu = 0
outputNumber = 0
memory = -1

exten = ".json"
topdir = "/home/alex/archive/food/new_archive/"

for path, subdirs, files in os.walk(topdir):
    for name in files:
	if exten in name.lower():
		n_name = (os.path.join(path, name))
        

    		print n_name
    		if cpu%8 == 0:
        		memory = (memory + 1) % 8	


		outputNumber += 1
		print file
		command =  "sudo numactl --membind={} --physcpubind={} sudo python ./deploy/tweet_processor.py {} {} &".format(memory, cpu, n_name, outputNumber)
    		os.system(command)
    		print command
    
    		cpu = (cpu + 1) % 64
