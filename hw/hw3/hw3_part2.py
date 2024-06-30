# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:54:21 2022

@author: Cam

Run a simulation of a pokemon with a given number of turns. Evrey turn, the
pokemon moves 5 steps in a given direction. Every set number of turns, the 
pokemon encounters another pokemon and fights it. Print the pokemon's final
position and win/loss record.
"""

def move_pokemon(location, direction, steps):
    '''
    Takes in location as a tuple (row, column), direction as a string, and 
    number of steps. Move the pokemon in the given direction with the given 
    number of steps. The new row and column must be greater than 0 and less
    than 150. Return the new location as a tuple.
    '''
    row, column = location
    if direction == 'n' or direction == 'N':
        row -= steps
    elif direction == 's' or direction == 'S':
        row += steps
    elif direction == 'w' or direction == 'W':
        column -= steps
    elif direction == 'e' or direction == 'E':
        column += steps
    row = max(row, 0)
    row = min(row, 150)
    column = max(column, 0)
    column = min(column, 150)
    return (row, column)


if __name__ == "__main__":
    #set starting values and inputs
    turns = input("How many turns? => ").strip()
    print(turns)
    turns = int(turns)
    
    name = input("What is the name of your pikachu? => ").strip()
    print(name)
    
    often = input("How often do we see a Pokemon (turns)? => ").strip()
    print(often)
    often = int(often)
    
    row = 75
    column = 75
    direction = 'n'
    record = []
    
    #main simulation loop
    print("")
    print("Starting simulation, turn 0 {} at (75, 75)".format(name))
    i = 0
    while i < turns:            
        i += 1
        direction = input("What direction does {} walk? => ".format(name)).strip()
        print(direction)
        row, column = move_pokemon((row, column), direction, 5)
        
        if i % often == 0 and i != 0:
            #start an encounter
            print("Turn {}, {} at ({}, {})".format(i, name, row, column))
            pType = input("What type of pokemon do you meet (W)ater, (G)round? => ").strip()
            print(pType)
            if pType == 'W' or pType == 'w':
                row, column = move_pokemon((row, column), direction, 1)
                print("{} wins and moves to ({}, {})".format(name, row, column))
                record.append("Win")
            elif pType == 'G' or pType == 'g':
                row, column = move_pokemon((row, column), direction, -10)
                print("{} runs away to ({}, {})".format(name, row, column))
                record.append("Lose")
            else:
                record.append("No Pokemon")
        
    #print the results
    print("{} ends up at ({}, {}), Record: {}".format(name, row, column, record))
            
    