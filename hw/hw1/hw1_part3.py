# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:02:52 2022

@author: eichc

Create a frame with an inputted height and width, using an inputted character.
"""

#ask for all inputs
character = input("Enter frame character ==> ").strip()
print(character)

height = input("Height of box ==> ").strip()
print(height)

width = input("Width of box ==> ").strip()
print(width)


dimensions = width + "x" + height
height = int(height)
width = int(width)

print("\nBox:")

#top half of frame
print(character*width)
topNumLines = (height - 3) // 2
print((character + " "*(width-2) + character + "\n")*topNumLines, end="")

#print the dimensions on a centered line
spaceBeforeDim = (width - 2 - len(dimensions)) // 2
spaceAfterDim = width - 2 - len(dimensions) - spaceBeforeDim
print(character, " "*spaceBeforeDim, dimensions, " "*spaceAfterDim, character,
      sep="")

#bottom half of frame
bottomNumLines = height - 3 - topNumLines
print((character + " "*(width-2) + character + "\n")*bottomNumLines, end="")
print(character*width)