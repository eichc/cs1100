# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:37:07 2022

@author: eichc
"""

import lab05_util

def print_info(restaurant):
    address = restaurant[3].split('+')
    total = sum(restaurant[-1])
    avg = total / len(restaurant[-1])
    
    #print the info
    print(restaurant[0], "({})".format(restaurant[5]))
    for line in address:
        print("\t" + line)
    print("Average score: {:.2f}".format(avg))

restaurants = lab05_util.read_yelp('yelp.txt')


#tests
print_info(restaurants[0])
print("")
print_info(restaurants[4])
print("")
print_info(restaurants[42])