# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:51:01 2022

@author: eichc
"""

# s1 = 'art'
# s2 = 'Art'
# s3 = 'Music'
# s4 = 'music'
# print(s1 < s2)
# print(s2 < s3)
# print(s2 < s4)
# print(s1 < s3)

x0 = 10
x1 = 16
y0 = 32
y1 = 45

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x0 < x < x1 and y0 < y < y1:
    print("Your point is inside the rectangle.")
elif (x == x0 or x == x1) and (y0 <= y <= y1):
    print("Your point is on the boundary.")
elif (y == y0 or y == y1) and (x0 <= x <= x1):
    print("Your point is on the boundary.")
else:
    print("Your point is outside the rectangle.")