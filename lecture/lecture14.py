# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:52:39 2022

@author: eichc
"""

'''
Given a list of non-negative numbers, find all pairs of indices for those 
elements whose difference equals k, where k is an integer. Output all pairs
as a list of tuples.
'''
# L = [0,1,5,2,3,10,9,6,4]
# k = 1

# #nest for loop
# #outside loop picks every index except last value
# #inner loop picks every index starting from i+1
# #if condition checks if absolute difference is k or not
# #if it equals k, append tuple with indices to result list

# result = []
# for i in range(len(L)-1):
#     for j in range(i+1, len(L)):
#         if abs(L[i] - L[j]) == k:
#             result.append((i, j))
# print(result)

'''
Find the mode of a set of numbers given as a list of tuples.
'''
scores = [(3, 2), (2, 1), (9, 1), (8, 7), (2, 0), (0,4), (1,7), (29, 6), \
          (27, 29), (30, 29), (2, 29)]

#create a new list without tuples
#sort the list
#loop through the list
    #create variable that counts consecutive numbers
    #save the count and the number if the count is greater than previous count
    #reset variable every time new number is encountered

new_scores = []
for i in range(len(scores)):
    new_scores.append(scores[i][0])
    new_scores.append(scores[i][1])
new_scores.sort()

modes = [new_scores[0]]
count = 1
max_count = 1
previous = new_scores[0]
for i in range(1, len(new_scores)):
    if new_scores[i] == new_scores[i-1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
            modes = [new_scores[i-1]]
        elif count == max_count:
            modes.append(new_scores[i-1])
        count = 1
    previous = new_scores[i]
print(modes)