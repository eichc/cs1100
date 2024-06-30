# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:27:03 2022

@author: eichc
Calculates the actual size of a hard drive given an input advertised size.
"""

base10size = input("Disk size in GB => ")
print(base10size)
base10size = int(base10size)

base2size = base10size * (10**9) // (2**30)
lost_size = base10size - base2size

print(base10size, "GB in base 10 is actually", base2size, "GB in base 2,", 
      lost_size, "GB less than advertised.")
print("Input: ", "*" * base10size)
print("Actual:", "*" * base2size)