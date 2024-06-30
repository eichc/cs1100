# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:09:44 2022

@author: eichc
"""

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
last = last + "!"

greetLen = len("Hello,")
firstLen = len(first)
lastLen = len(last)

maxLen = max(greetLen, firstLen, lastLen)

print("*"*(maxLen + 6))
print("** ", "Hello,", " "*(maxLen-greetLen), " **", sep="")
print("** ", first, " "*(maxLen-firstLen), " **", sep="")
print("** ", last, " "*(maxLen-lastLen), " **", sep="")
print("*"*(maxLen + 6))

