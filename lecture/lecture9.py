# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:51:31 2022

@author: eichc
"""

#while loop using a flag:
total = 0
end_found = False

while not end_found:
    x = int( input("Enter an integer to add (0 to end) ==> "))
    if x == 0:
        end_found = True
    else:
        total += x

print(total)