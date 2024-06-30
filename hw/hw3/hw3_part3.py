# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:23:25 2022

@author: eichc
"""
import math

def num_tourists(bears):
    '''
    Calculate and return the number of tourists given a number of bears.
    '''
    if bears < 4 or bears > 15:
        return 0
    elif 4 <= bears <= 10:
        return 10000 * bears
    else:
        return 100000 + (bears-10)*20000

def find_next(bears, berries, tourists):
    '''
    Given a number of bears, berries, and tourists, calculate next year's
    number of bears and berries. All values must be non-negative, and bears and
    tourists must be integers.
    '''
    bears_next = berries/(50*(bears+1)) + bears*0.60- \
        (math.log(1+tourists,10)*0.1)
    bears_next = math.floor(bears_next)
    bears_next = max(bears_next, 0)
    berries_next = (berries*1.5)- (bears+1)*(berries/14)- \
        (math.log(1+tourists,10)*0.05)
    berries_next = max(berries_next, 0)
    return (bears_next, berries_next)

def make_columns(w1, w2, w3, w4):
    '''
    Takes in 4 strings and prints them in four columns of ten characters each.
    '''
    c1 = w1 + " "*(10-len(w1))
    c2 = w2 + " "*(10-len(w2))
    c3 = w3 + " "*(10-len(w3))
    c4 = w4 + " "*(10-len(w4))
    print(c1 + c2 + c3 + c4)
    return


if __name__ == "__main__":
    #inputs and initial values
    bears = input("Number of bears => ").strip()
    print(bears)
    bears = int(bears)
    
    berries = input("Size of berry area => ").strip()
    print(berries)
    berries = float(berries)
    
    tourists = num_tourists(bears)
    
    #initialize a list for each population to determine max and min
    list_bears = [bears]
    list_berries = [berries]
    list_tourists = [tourists]
    
    #print the populations for the first year
    make_columns("Year", "Bears", "Berry", "Tourists")
    make_columns("1", str(bears), str(round(berries, 1)), str(tourists))
    
    #print the populations for the next 9 years
    for i in range(9):
        bears, berries = find_next(bears, berries, tourists)
        tourists = num_tourists(bears)
        make_columns(str(i + 2), str(bears), str(float(round(berries, 1))), str(tourists))
        
        #add each population to its respective list
        list_bears.append(bears)
        list_berries.append(berries)
        list_tourists.append(tourists)
        
    
    #find the max and min of each population
    max_berries = round(max(list_berries), 1)
    min_berries = round(min(list_berries), 1)
    max_bears = max(list_bears)
    min_bears = min(list_bears)
    max_tourists = max(list_tourists)
    min_tourists = min(list_tourists)
    
    #print the max and min of each population
    print("")
    make_columns("Min:", str(min_bears), str(min_berries), str(min_tourists))
    make_columns("Max:", str(max_bears), str(max_berries), str(max_tourists))