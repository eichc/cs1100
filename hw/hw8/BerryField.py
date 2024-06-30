# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:05:29 2022

@author: Cam Eich

A berry field is a grid that contains berries, bears, and tourists. The
berries can grow and spread.
"""

class BerryField(object):
    def __init__(self, grid):
        '''
        Initialize a berry field, taking in a grid as a list of lists.
        '''
        self.grid = list(grid)
    
    def __str__(self):
        '''
        Print the berry field as a grid, with each location formatted to 4
        characters.
        '''
        string = ''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                string += "{:>4}".format(self.grid[i][j])
            string += '\n'
        return string
    
    def copy(self):
        '''
        Returns a copy of the berry field.
        '''
        #first, create a field of the same size with all empty values
        L = []
        for i in range(len(self.grid)):
            L.append([])
            for j in range(len(self.grid[0])):
                L[i].append(0)
                
        #copy all values from the field into L
        for i in range(len(L)):
            for j in range(len(L[0])):
                L[i][j] = self.grid[i][j]
        return BerryField(L)

    def grow(self):
        '''
        Increase the number of berries by 1 in every location that has less
        than 10 berries.
        '''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if str(self.grid[i][j]).isnumeric() and 1 <= self.grid[i][j] < 10:
                    self.grid[i][j] += 1
    
    def spread(self):
        '''
        Any location with no berries that is adjacent to a location with 10 
        berries will gain 1 berry.
        '''
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    #ensure each adjacent location exists, then check if it has
                    #10 berries
                    if i-1 > -1 and self.grid[i-1][j] == 10:
                        self.grid[i][j] = 1
                    elif i+1 < len(self.grid) and self.grid[i+1][j] == 10:
                        self.grid[i][j] = 1
                    elif j-1 > -1 and self.grid[i][j-1] == 10:
                        self.grid[i][j] = 1
                    elif j+1 < len(self.grid[0]) and self.grid[i][j+1] == 10:
                        self.grid[i][j] = 1
                    elif i-1 > -1 and j-1 > -1 and self.grid[i-1][j-1] == 10:
                        self.grid[i][j] = 1
                    elif i-1 > -1 and j+1 < len(self.grid[0]) and \
                        self.grid[i-1][j+1] == 10:
                            self.grid[i][j] = 1
                    elif i+1 < len(self.grid) and j-1 > -1 and \
                        self.grid[i+1][j-1] == 10:
                            self.grid[i][j] = 1
                    elif i+1 < len(self.grid) and j+1 < len(self.grid[0]) and \
                        self.grid[i+1][j+1] == 10:
                            self.grid[i][j] = 1