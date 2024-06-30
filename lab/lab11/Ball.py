# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:47:18 2022

@author: eichc
"""

class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.ogx = x
        self.y = y
        self.ogy = y
        self.dx = dx
        self.ogdx = dx
        self.dy = dy
        self.ogdy = dy
        self.radius = radius
        self.color = color
        
    def position(self):
        return (self.x, self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        return (self.x-self.radius, self.y-self.radius, self.x+self.radius, 
                self.y+self.radius)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        return 0 < self.x + self.radius and self.x - self.radius < maxx \
               and 0 < self.y + self.radius and self.y - self.radius < maxy
    
    def check_and_reverse(self, maxx, maxy):
        if self.x + self.radius > maxx or self.x - self.radius < 0:
            self.dx *= -1
        if self.y + self.radius > maxy or self.y - self.radius < 0:
            self.dy *= -1