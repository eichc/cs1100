# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:06:09 2022

@author: eichc
"""

word = input("Enter a word: ")

frameLen = len(word) + 6
print("*"*frameLen)
print("**", word, "**")
print("*"*frameLen)