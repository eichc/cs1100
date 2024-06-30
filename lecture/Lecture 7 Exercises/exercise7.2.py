# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:19:21 2022

@author: eichc
"""

def add_tuples(a, b, c):
    '''
    Take three tuples and return a single tuple containing the sum.
    '''
    sum1 = a[0] + b[0] + c[0]
    sum2 = a[1] + b[1] + c[1]
    return (sum1, sum2)

if __name__ == "__main__":
    print(add_tuples( (1,4), (8,3), (14,0) ))
    print(add_tuples( (3,2), (11,1), (-2,6) ))