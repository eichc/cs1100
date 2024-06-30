# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:04:52 2022

@author: Cam Eich

Create the berry field, bear, and tourist objects contained in the json file.
Then, print out the berry field, active bears, and active tourists.
"""
import json
from BerryField import *
from Bear import *
from Tourist import *

if __name__ == "__main__":    
    file = input("Enter the json file name for the simulation => ").strip()
    print(file)
    
    f = open(file)
    data = json.loads(f.read())
    
    #create objects
    field = BerryField(data["berry_field"])
    
    active_bears = []
    reserve_bears = []
    for bear in data["active_bears"]:
        active_bears.append(Bear(bear[0], bear[1], bear[2]))
    for bear in data["reserve_bears"]:
        reserve_bears.append(Bear(bear[0], bear[1], bear[2]))
        
    active_tourists = []
    reserve_tourists = []
    for tourist in data["active_tourists"]:
        active_tourists.append(Tourist(tourist[0], tourist[1]))
    for tourist in data["reserve_tourists"]:
        reserve_tourists.append(Tourist(tourist[0], tourist[1]))
    
    #calculate total berries
    total_berries = 0
    for i in range(len(field.grid)):
        for j in range(len(field.grid[0])):
            if str(field.grid[i][j]).isnumeric():
                total_berries += field.grid[i][j]
    print("\nField has {} berries.".format(total_berries))
    
    #add bears and tourists to the field
    for bear in active_bears:
        field.grid[bear.row][bear.col] = 'B'
    for tourist in active_tourists:
        if field.grid[tourist.row][tourist.col] == 'B':
            field.grid[tourist.row][tourist.col] = 'X'
        else:
            field.grid[tourist.row][tourist.col] = 'T'
    
    #print the berry field
    print(field)
    
    #print bears
    print("Active Bears:")
    for bear in active_bears:
        print(bear)
    
    #print tourists
    print("\nActive Tourists:")
    for tourist in active_tourists:
        print(tourist)