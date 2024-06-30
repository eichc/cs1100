# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:47:33 2022

@author: eichc

Write a function that takes a Celsius temperature and converts it to Fahrenheit.
Call the function 3 times, with 0, 32, and 100.
"""

def convert2fahren(c):
    return c * (9/5) + 32

print(0, "->", convert2fahren(0))
print(32, "->", convert2fahren(32))
print(100, "->", convert2fahren(100))