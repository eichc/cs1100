# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:09:54 2022

@author: eichc

Determine if a list is in increasing order.
"""
def is_increasing(values):
    for i in range(len(values)-1):
        if values[i] > values[i+1]:
            return False
    return True


co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))
test_L1 = [ 15, 12, 19, 27, 45 ]
print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
test_L2 = [ 'arc', 'circle', 'diameter', 'radius', 'volume', 'area' ]
print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
test_L3 = [ 11, 21, 19, 27, 28, 23, 31, 45 ]
print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))