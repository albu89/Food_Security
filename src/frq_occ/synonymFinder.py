'''
Created on Mar 30, 2015

@author: alexanderbusser
'''
import nltk
from nltk.corpus import wordnet as wn

def syn(word, lch_threshold=2):
    wn.synsets(word);
    for net1 in wn.synsets(word):
        for net2 in wn.all_synsets():
            try:
                lch = net1.lch_similarity(net2)
            except:
                continue
            # The value to compare the LCH to was found empirically.
            # (The value is very application dependent. Experiment!)
            if lch >= lch_threshold:
                yield (net1, net2, lch)
                
                


def main():
   
  
    for x in syn('available'): 
        print x
    
    

if __name__ == '__main__':
    main()