# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:54:32 2022

@author: eichc
"""

# scores = [59, 61, 63, 63, 68, 64, 58]
# print(scores)

# #indexing lists:
# print(sum(scores)/len(scores)) #average
# print(scores[-1]) #negative index goes back to front
# print(scores[len(scores)//2]) #index of middle
# scores[0] = 60 #Lists are mutable

# #sorting lists:
# scores.sort() #sort does not return a value, changes the original list
# print(scores)
# #OR
# print(sorted(scores)) #sorted returns the sorted list but does not change the original list

# #Mutating lists:
# scores.append(70)
# scores.insert(0, 62)
# print(scores)
# s = scores.pop(2) #removes the element at specified index and returns it
# print(s)
# print(scores)
# scores.remove(59) #removes first occurence of specified value
# print(scores)

#nested lists:
L = ['Alice', 3.75, ['MATH', 'CSCI', 'PSYC' ], 'PA']
print(L[2])
print(L[2][0])
L[2].append('STAT')
print(L)