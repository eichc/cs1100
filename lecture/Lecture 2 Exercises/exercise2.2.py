# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:17:45 2022

@author: eichc

Calculate and print the volume and surface area of a box
"""

length = 16.5
width = 12.5
height = 5

volume = length * width * height
surfaceArea = 2*(length*width + length*height + width*height)

print("volume =", volume)
print("area =", surfaceArea)