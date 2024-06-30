# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 13:09:48 2022

@author: eichc

# description of the program
Ask the user for their name, ask for a radius and height of a cylinder, and finally
compute the volume
"""

# all import statements
import math

# all function definitions
def exampleFunction():
    '''
    
    Brief description
    '''
    pass

if __name__ == "__main__": #guard
    # all variables and input
    name = input("Please enter your name: ").strip()
    radius = input("Enter the radius: ")
    radius = float(radius)
    height = input("Enter the height: ")
    height = float(height)

    # all computations
    volume = math.pi*(radius**2)*height

    # all output
    print("Volume = {:.2f}".format(volume))