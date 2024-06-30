# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:42:36 2022

@author: eichc
"""

#Calculate volume and surface area of a cylinder
pi = 3.14159
radius = 2
height = 5
baseArea = pi * (radius**2)
volume = baseArea * height
surfaceArea = (2 * baseArea) + (2 * pi * radius * height)
print("The volume is", volume, "and the surface area is", surfaceArea)