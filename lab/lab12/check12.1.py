# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:44:18 2022

@author: eichc
"""

def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m,n):
    if n == 0:
        return 0
    else:
        return add(mult(m,n-1), m)

def power(m,n):
    if n == 0:
        return 1
    else:
        return mult(power(m,n-1), m)
    
if __name__ == "__main__":
    print(add(5,3))
    print(mult(8,3))
    print(power(6,3))