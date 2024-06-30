# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:34:04 2022

@author: Cam Eich

Print the initial state of the simulation. Then, run 5 turns of the simulation,
ignoring the reserve bears and tourists. In each turn the berries grow/spread,
the bears move, the tourists are updated, and the results are printed.
"""

import json
from BerryField import *
from Bear import *
from Tourist import *


def move_bears(bearList, touristList, field):
    '''
    Given a list of bears, move each of them until they have consumed 30
    berries, left the field, or encountered a tourist. Return a list of bears
    that have left the field.
    '''
    left_field = []
    for bear in bearList:
        #variable to check if bear is still in field
        in_field = 0 <= bear.row < len(field.grid) and \
            0 <= bear.col < len(field.grid[0])

        #skip the turn if the bear is asleep
        if bear.sleep > 0:
            bear.sleep -= 1
            continue
        
        #eat a berry or move if there are no berries left
        while bear.berries_eaten < 30 and in_field and not \
            bear.check_for_tourist(touristList):
                if field.grid[bear.row][bear.col] > 0:
                    field.grid[bear.row][bear.col] -= 1
                    bear.berries_eaten += 1
                else:
                    bear.move()
                #update in_field with bear's new location
                in_field = 0 <= bear.row < len(field.grid) and \
                    0 <= bear.col < len(field.grid[0])
        bear.berries_eaten = 0
        
        if bear.check_for_tourist(touristList):
            bear.sleep = 2
        if not in_field:
            left_field.append(bear)

    return left_field

def check_tourists(touristList, bearList, field):
    '''
    Check each tourist to see if it sees 3 bears, hasn't seen a bear in 3
    turns, or is in the same space as a bear. If any of these are true,
    add the tourist to a list that will be returned.
    '''
    left_field = []
    for tourist in touristList:
        if tourist.bear_encounter(bearList):
            left_field.append(tourist)
        elif tourist.check_for_bears(bearList) >= 3:
            left_field.append(tourist)
        elif tourist.turns_since_bear == 3:
            left_field.append(tourist)
            
    return left_field


if __name__ == "__main__":    
    file = input("Enter the json file name for the simulation => ").strip()
    print(file)
    
    f = open(file)
    data = json.loads(f.read())
    
    print("\nStarting Configuration")
    
    #create objects
    field = BerryField(data["berry_field"]) #the field that stores all berries
    display = field.copy() #the field that will be printed
    
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
            total_berries += field.grid[i][j]
    print("Field has {} berries.".format(total_berries))
    
    #add bears and tourists to the display
    for bear in active_bears:
        display.grid[bear.row][bear.col] = 'B'
    for tourist in active_tourists:
        if display.grid[tourist.row][tourist.col] == 'B':
            display.grid[tourist.row][tourist.col] = 'X'
        else:
            display.grid[tourist.row][tourist.col] = 'T'
    
    #print the initial berry field, bears, and tourists
    print(display)
    
    print("Active Bears:")
    for bear in active_bears:
        print(bear)
    
    print("\nActive Tourists:")
    for tourist in active_tourists:
        print(tourist)
        
        
    #run 5 turns
    for i in range(5):
        print("\nTurn:", i+1)
        #grow the berries
        field.grow()
        field.spread()
        
        #move the bears and remove the bears that have left the field
        bears_left = move_bears(active_bears, active_tourists, field)
        for bear in bears_left:
            active_bears.remove(bear)
        
        #check on tourists and remove tourists that left the field
        tourists_left = check_tourists(active_tourists, active_bears, field)
        for tourist in tourists_left:
            active_tourists.remove(tourist)
        
        #calculate total berries
        total_berries = 0
        for i in range(len(field.grid)):
            for j in range(len(field.grid[0])):
                total_berries += field.grid[i][j]
        
        #update display
        display = field.copy()
        for bear in active_bears:
            display.grid[bear.row][bear.col] = 'B'
        for tourist in active_tourists:
            if display.grid[tourist.row][tourist.col] == 'B':
                display.grid[tourist.row][tourist.col] = 'X'
            else:
                display.grid[tourist.row][tourist.col] = 'T'
        
        #print state of simulation
        for bear in bears_left:
            print("{} - Left the Field".format(bear))
        for tourist in tourists_left:
            print("{} - Left the Field".format(tourist))
        print("Field has {} berries.".format(total_berries))
        print(display)
        print("Active Bears:")
        for bear in active_bears:
            print(bear)
        print("\nActive Tourists:")
        for tourist in active_tourists:
            print(tourist)
        print()