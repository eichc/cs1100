# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 10:33:51 2022

@author: eichc

Construct a Mad Lib with the given prompt
"""

def prompt(s):
    '''
    Prompts the user for an input of a given part of speech.
    '''
    word = input(s + " ==> ").strip()
    print(word)
    return word


print("Let's play Mad Libs for Homework 1")
print("Type one word responses to the following:\n")

#recieve all inputs for the Mad Lib
properName = prompt("proper_name")
adj1 = prompt("adjective")
noun1 = prompt("noun")
verb1 = prompt("verb")
verb2 = prompt("verb")
noun2 = prompt("noun")
emotion1 = prompt("emotion")
verb3 = prompt("verb")
noun3 = prompt("noun")
season = prompt("season")
adj2 = prompt("adjective")
emotion2 = prompt("emotion")
teamName = prompt("team-name")
noun4 = prompt("noun")
adj3 = prompt("adjective")

#print the Mad Lib
print("\nHere is your Mad Lib...\n")
print("Good morning ", properName, "!", sep="", end="\n\n")
print("\tThis will be a/an ", adj1, " ", noun1, "! Are you ", verb1, 
      " forward to it?", sep="")
print("\tYou will", verb2, "a lot of", noun2, "and feel", emotion1, 
      "when you do.")
print("\tIf you do not, you will " + verb3 + " this " + noun3 + ".\n")
print("\tThis ", season, " was ", adj2, ". Were you ", emotion2, " when ", 
      teamName, " won", sep="")
print("\tthe ", noun4, "?", sep="", end="\n\n")
print("\tHave a/an", adj3, "day!")