# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:44:27 2022

@author: eichc
"""

def get_words(description):
    desc = description.replace('.',' ')
    desc = desc.replace(',',' ')
    desc = desc.replace('(',' ')
    desc = desc.replace(')',' ')
    desc = desc.replace('"',' ')
    desc = desc.lower()
    L = desc.split()
    for i in range(len(L)-1, -1, -1):
        if not (L[i].isalpha() and len(L[i]) >= 4):
            L.remove(L[i])
    return set(L)

wrpi = open('wrpi.txt')
wrpi_str = wrpi.read()
wrpi_desc = wrpi_str.split('|')[1]
wrpi_words = get_words(wrpi_desc)
print("Length:", len(wrpi_words))
print(wrpi_words)