# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:52:57 2022

@author: eichc

Calculate the number of values in a list that are greater than the average.
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
avg = sum(co2_levels) / len(co2_levels)
numGreater = 0

for n in co2_levels:
    if n > avg:
        numGreater += 1

print("Average: {:.2f}".format(avg))
print("Num above average:", numGreater)