# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:30:37 2022

@author: eichc
"""

hd = input("Enter Dale's height: ").strip()
print(hd)
hd = int(hd)

he = input("Enter Erin's height: ").strip()
print(he)
he = int(he)

hs = input("Enter Sam's height: ").strip()
print(hs)
hs = int(hs)


#determine the order of the heights
heights = [hd, he, hs]
first = max(heights)
third = min(heights)
second = sum(heights) - first - third


#print the heights in order
if first == hd:
    print("Dale")
elif first == he:
    print("Erin")
else:
    print("Sam")

if second == hd:
    print("Dale")
elif second == he:
    print("Erin")
else:
    print("Sam")
    
if third == hd:
    print("Dale")
elif third == he:
    print("Erin")
else:
    print("Sam")