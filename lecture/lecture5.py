# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:53:05 2022

@author: eichc
"""

import math

# # #Write a function to compute area of a circle
# def areaCircle(radius):
#     area = math.pi*(radius**2)
#     return round(area,2)
# # print(areaCircle(float(input("Enter a radius: "))))


# #Convert mph to kilometers per day
# def convert(mph):
#     return 1.6*24*mph


# #Compute surface area of a cylinder using 2 functions
# def areaCircle(radius):
#     return math.pi * (radius**2)

# def areaCylinder(radius, height):
#     circleArea = areaCircle(radius)
#     heightArea = 2 * radius * math.pi * height
#     return (2 * circleArea) + heightArea

# print('The area of a circle of radius 1 is', round(areaCircle(1),2))
# r = 2
# height = 10
# print('The surface area of a cylinder with radius', r, end=' ')
# print('and height', height, 'is', round(areaCylinder(r,height),2))


# #Return the middle value of 3 integers
# def middleValue(a, b, c):
#     sum = a + b + c
#     sum -= max(a, b, c)
#     sum -= min(a, b, c)
#     return sum


#Scale a score without exceeding 100
def scale(raw, a, b):
    scaled = (a * raw) + b
    return min(100, scaled)