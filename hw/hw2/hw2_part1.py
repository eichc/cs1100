# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:49:42 2022

@author: eichc

Create a gum ball machine, and calculate various values for it using an inputted gum ball
radius and number of weekly sales.
"""
import math

def find_volume_sphere(radius):
    '''
    
    Return the volume of a sphere given the radius.
    '''
    return (4/3) * math.pi * radius**3

def find_volume_cube(side):
    '''
    
    Return the volume of a cube given the side length.
    '''
    return side**3

if __name__ == "__main__":
    #ask for inputs
    radius = input("Enter the gum ball radius (in.) => ").strip()
    print(radius)
    radius = float(radius)

    sales = input("Enter the weekly sales => ").strip()
    print(sales)
    sales = int(sales)


    targetSales = math.ceil(1.25 * sales)
    gbPerSide = math.ceil(math.pow(targetSales, 1/3)) #minimum gum balls along each dimension
    totalGB = find_volume_cube(gbPerSide) #total number of gum balls that will fit
    extraGB = totalGB - targetSales
    cubeSideLength = gbPerSide*radius*2 #side length of the machine
    cubeVolume = find_volume_cube(cubeSideLength) #volume of the machine
    gbVolume = find_volume_sphere(radius) #volume of each gum ball
    #wasted space inside the machine:
    wastedSpaceTarget = cubeVolume - (targetSales * gbVolume) 
    wastedSpaceFilled = cubeVolume - (totalGB * gbVolume)

    #print the results
    print("")
    print("The machine needs to hold {} gum balls along each edge.".format(gbPerSide))
    print("Total edge length is {:.2f} inches.".format(cubeSideLength))
    print("Target sales were {}, but the machine will hold {} extra gum balls.".format(targetSales, extraGB))
    print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(wastedSpaceTarget))
    print("or {:.2f} cubic inches if you fill up the machine.".format(wastedSpaceFilled))