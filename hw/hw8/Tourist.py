# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:05:53 2022

@author: Cam Eich

A tourist does not move, and they leave the field if they are bored or scared.
They mysteriously disappear if they encounter a bear.
"""

class Tourist(object):
    def __init__(self, row, col):
        '''
        Initialize a tourist, taking in a location.
        '''
        self.row = row
        self.col = col
        self.turns_since_bear = 0
    
    def __str__(self):
        '''
        Print the tourist's locaiton and how long since they have seen a bear.
        '''
        return "Tourist at ({},{}), {} turns without seeing a bear.".format( \
                self.row, self.col, self.turns_since_bear)
    
    def check_for_bears(self, bearList):
        '''
        Return as an int the number of bears the tourist sees. Update
        turns_since_bear.
        '''
        bears = 0
        for bear in bearList:
            if ((self.col-bear.col)**2 + (self.row-bear.row)**2)**0.5 <= 4:
                bears += 1
                self.turns_since_bear = 0
        if bears == 0:
            self.turns_since_bear += 1
        return bears
    
    def bear_encounter(self, bearList):
        '''
        Check if the tourist is in the same location as a bear.
        '''
        for bear in bearList:
            if self.row == bear.row and self.col == bear.col:
                return True
        return False