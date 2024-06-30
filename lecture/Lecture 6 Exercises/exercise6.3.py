# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:59:05 2022

@author: eichc

Calculate the average of two numbers, one of which must be greater than 10
and the other must be less than 10.
"""
#all inputs
first = input("Enter the first number: ").strip()
print(first)
first = float(first)

second = input("Enter the second number: ").strip()
print(second)
second = float(second)

#print any error messages
if first > 10 and second > 10:
    print("Both are above 10.")
elif first < 10 and second < 10:
    print("Both are below 10.")
    
#print the average
average = (first + second) / 2
print("Average is {:.2f}".format(average))