# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:54:34 2022

@author: eichc
"""

file = input("Data file name: ").strip()
print(file)

prefix = input("Prefix: ").strip()
print(prefix)

names = set()
prefix_names = set()
for line in open(file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip().split(',')
    last_name = name[0]
    if last_name != '':
        names.add(last_name)
    if last_name.find(prefix) == 0:
        prefix_names.add(last_name)

print("{} last names".format(len(names)))
print("{} start with {}".format(len(prefix_names), prefix))