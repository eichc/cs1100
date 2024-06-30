# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:15:30 2022

@author: eichc
"""

scores = input("Enter the scores file: ").strip()
print(scores)

sorted_file = input("Enter the output file: ").strip()
print(sorted_file)


s = []
for line in open(scores):
    score = line.strip()
    score = int(score)
    s.append(score)
s.sort()

w = open(sorted_file, 'w')
for i in range(len(s)):
    w.write("{:2d}: {:3d}\n".format(i, s[i]))