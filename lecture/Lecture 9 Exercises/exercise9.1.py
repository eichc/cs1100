# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:25:22 2022

@author: eichc

Print all multiples of 3 that are less than an inputted number.
"""

num = input("Enter a positive integer: ").strip()
print(num)
num = int(num)

i = 0
while i < num:
    print(i)
    i+=3