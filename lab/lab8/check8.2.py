# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:57:41 2022

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

club1 = open('wrpi.txt').read()
club1_name = club1.split('|')[0]
club1_desc = club1.split('|')[1]
words1 = get_words(club1_desc)

club2 = open('csa.txt').read()
club2_name = club2.split('|')[0]
club2_desc = club2.split('|')[1]
words2 = get_words(club2_desc)

common = words1.intersection(words2)
unique1 = words1.difference(words2)
unique2 = words2.difference(words1)
        
print("Comparing clubs {} and {}:".format(club1_name, club2_name))
print('')
print("Same words: {}".format(common))
print('')
print("Unique to {}: {}".format(club1_name, unique1))
print('')
print("Unique to {}: {}".format(club2_name, unique2))
