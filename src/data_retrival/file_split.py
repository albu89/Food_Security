  '''
@author: albu

'''


import os,sys

name  = sys.argv[1]

newDir = name[:-5]


command = "split -l 20000 {} {}/{}".format(name,newDir, name)

os.system(command)
