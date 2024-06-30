# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:37:45 2022

@author: eichc

Create a list of inputted numbers until the user types a 0.
Print the min, max, and average of the list.
"""

nums = []
zeroEntered = False
while not zeroEntered:
    num = input("Enter a value (0 to end): ").strip()
    print(num)
    num = int(num)
    
    if num == 0:
        zeroEntered = True
    else:
        nums.append(num)

print("Min: {}".format(min(nums)))
print("Max: {}".format(max(nums)))
print("Avg: {:.1f}".format(sum(nums) / len(nums)))