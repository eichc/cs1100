# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:28:35 2022

@author: eichc

Calculate the average percent change in the population of New York State
between 1790 and 2010.
"""

census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
            5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
            8236, 17558, 17990, 18976, 19378 ]
    
i = 0
sumPercentChange = 0
while i < len(census) - 1:
    percentChange = (census[i+1] - census[i]) / census[i] * 100
    sumPercentChange += percentChange
    i+=1

avg = sumPercentChange / (len(census) - 1)
print("Average = {:.1f}%".format(avg))