# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:05:39 2022

@author: Cam Eich

A bear moves in a straight line until it eats 30 berries, leaves the field,
or encounters a tourist. If it encounters a tourist, it falls asleep for 3
turns.
"""
from Tourist import *

class Bear(object):
    def __init__(self, row, col, direction):
        '''
        Initialize a bear, taking in a location and movement direction.
        '''
        self.row = row
        self.col = col
        self.direction = direction
        self.sleep = 0
        self.berries_eaten = 0
    
    def __str__(self):
        '''
        Print the location and direction of the bear, and if it is asleep.
        '''
        string = "Bear at ({},{}) moving {}".format(self.row, self.col, \
                                                    self.direction)
        if self.sleep > 0:
            string += " - Asleep for {} more turns".format(self.sleep)
        return string
    
    def move(self):
        '''
        Move the bear one space in the direction it is facing.
        '''
        if self.direction == 'NE' or self.direction == 'N' or \
        self.direction == 'NW':
            self.row -= 1
        if self.direction == 'SE' or self.direction == 'S' or \
        self.direction == 'SW':
            self.row += 1
        if self.direction == 'NE' or self.direction == 'E' or \
        self.direction == 'SE':
            self.col += 1
        if self.direction == 'NW' or self.direction == 'W' or \
        self.direction == 'SW':
            self.col -= 1
    
    def check_for_tourist(self, touristList):
        '''
        Check if the bear is in the same location as a tourist.
        '''
        for tourist in touristList:
            if self.row == tourist.row and self.col == tourist.col:
                return True
        return False
    