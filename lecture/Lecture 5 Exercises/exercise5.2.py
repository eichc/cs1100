# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:15:52 2022

@author: eichc

Write a function to print an inputed statement with a frame around it.
Call the function twice, with "Spanish Inquisition" and "Ni".
"""

def frame_string(s):
    print("*" * (len(s) + 6))
    print("**", s, "**")
    print("*" * (len(s) + 6))

frame_string("Spanish Inquisition")
print("")
frame_string("Ni")