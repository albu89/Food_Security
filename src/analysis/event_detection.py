'''
Created on May 17, 2015
@author: alexanderbusser
What does it do: Scripts finds peaks. We declare a peak if vi
deviates more than 2 median average deviations (MAD) from mean
Data Source: data/event_detection
'''


import csv
from numpy import mean, median


"""Read CSV"""
def read_csv():
    reader = csv.reader(open('/Users/alexanderbusser/Food_Security/data/event_detection/agg_needs.csv', 'rU'))
    counter = csv.reader(open('/Users/alexanderbusser/Food_Security/data/event_detection/agg_needs.csv', 'rU'))
    row_count = sum(1 for row in counter )
    return reader, row_count



"""Perform calculations within a given window size"""
def window(count):
    values = []
    total = []; inc = 0;
    c_data, row_count = read_csv() 
    if (row_count - count) <= 15    :
        return 0, 0
     
    for rows in c_data:
        if inc in range(count - 15, count + 16):
            try:
                values.append(int(rows[1]))
            except:
                continue   
        inc+=1
    med = median(values)

    
    for item in values: 
        total.append(abs(item - med))
        
    mean = sum(values)/len(values) 
    mad = median(total)
    
    return mean, mad
    

""" Finds peaks"""
def detect_peak(data):
    count = 0
    event = []
    for rows in data:
        count += 1
        if count < 45:
            continue
        mean, mad = window(count)
       
        if mean == 0 or mad == 0:
            continue
        
        deviation = (int(rows[1]) - mean)
        print "Deviation {} mean {} mad {}".format( deviation , mean, mad)
        
        if deviation > 2 * mad:
            event.append(rows[0])
            continue
    
    print "Number of spikes {}".format(len(event))
    for element in event:
        print element
       
 

def main ():
    data, row_count = read_csv()
    detect_peak(data)

"""Execute Script"""
main()