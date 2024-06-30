# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:00:07 2022

@author: eichc

Practice manipulating lists in various ways.
"""

values = [ 14, 10, 8, 19, 7, 13 ]

#1
num = input("Enter a value: ")
print(num)
num = int(num)
values.append(num)

#2
num2 = input("Enter another value: ")
print(num2)
num2 = int(num2)
values.insert(2, num2)

#3
print(values[3], values[-1])

#4
print("Difference:", max(values) - min(values))

#5
avg = sum(values) / len(values)
print("Average: {:.1f}".format(avg))

#6
values.sort()
mid1 = values[len(values)//2 - 1]
mid2 = values[len(values)//2]
median = (mid1 + mid2) / 2
print("Median: {:.1f}".format(median))