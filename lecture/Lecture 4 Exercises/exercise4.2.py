# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:11:28 2022

@author: eichc

Computes the areas of 2 circles in 2 different ways
"""

import math

radius1 = 5
radius2 = 32

area1 = math.pi*(radius1**2)
area2 = math.pi*pow(radius2, 2)

print("Area 1 = {:.2f}".format(area1))
print("Area 2 =", round(area2, 2))