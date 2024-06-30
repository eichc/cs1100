# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:46:20 2022

@author: eichc
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1


names = sorted(counts)
high_count = 0
high_name = ''
single_count = 0
for i in range(len(names)):
    name = names[i]
    if counts[name] > high_count:
        high_count = counts[name]
        high_name = name
    if counts[name] == 1:
       single_count += 1 

print("{} appears most often: {} times".format(high_name, high_count))
print("{} people appear once".format(single_count))