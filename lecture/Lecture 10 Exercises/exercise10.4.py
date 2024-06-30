# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:59:22 2022

@author: eichc

Increase all values of a list by a given fraction.
"""
def increaseFrac(values, p):
    for i in range(len(values)):
        values[i] *= (1+p)

p = input("Enter the fraction: ").strip()
print(p)
p = float(p)

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

increaseFrac(co2_levels, p)
    
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))