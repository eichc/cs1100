# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:56:52 2022

@author: eichc
"""

#2 parts of a class:
    #data representation / attributes (elements, characters, etc.)
    #interaction (.methods)

import math

class Point2d(object):
    def __init__(self, x0=0, y0=0): #setting default values avoids error if no parameters are given
        self.x = x0
        self.y = y0
    
    def magnitude(self): #distance from origin
        return math.sqrt(self.x**2 + self.y**2)
    
    def dist(self, other): #distance between 2 pointsh
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def scale(self, s):
        self.x *= s
        self.y *= s
    
    def dominates(self, other): #are both x and y of self > other
        return self.x > other.x and self.y > other.y
    
    def __str__(self): #tells how to format print method
        return '({}, {})'.format(self.x, self.y)
    
    def __add__(self, other): #tells how to use +
        return Point2d(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other): #tells how to use ==
        return self.x == other.x and self.y == other.y

p = Point2d(3, 5)
q = Point2d(4, 5)
print(p.magnitude())
print(p.dist(q))
print(p)
print(p+q)