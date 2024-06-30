# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:32:42 2022

@author: eichc
"""

import math

def circle(radius):
    ''' Compute and return the area of a circle '''
    return math.pi * radius**2

def cylinder(radius,height):
    ''' Compute and return the surface area of a cylinder '''
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area

def sphere(radius):
    '''  Compute and return the surface area of a sphere '''
    return 4 * math.pi * radius**2

if __name__ == "__main__":
    r = float(input("Enter the radius (float) => "))
    h = float(input("Enter the height (float) => "))
    print("Surface area is: {:.2f}".format(cylinder(10, 12)))
    print("Volume is: {:.2f}".format(h * circle(r)))