# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:07:24 2022

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

csa = open('wrpi.txt').read()
csa_name = csa.split('|')[0]
csa_desc = csa.split('|')[1]
csa_words = get_words(csa_desc)

similar_lens = []
for line in open('allclubs.txt'):
    name = line.split('|')[0]
    desc = line.split('|')[1]
    words = get_words(desc)
    if name != csa_name:
        common = words.intersection(csa_words)
        similar_lens.append((len(common), name))

similar_lens.sort(reverse=True)
print("Similar clubs:")
for i in range(5):
    print(similar_lens[i][1])