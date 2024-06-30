# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:46:36 2022

@author: eichc
"""
#map applies the first parameter(function) to the second(iterable)
#return list of squared values
#lambda means temporary function
#lambda parameter: return value
L = [1,2,3,4]
print(list(map(lambda x: x**2, L)))


#filter keeps only certain values from the iterable
#first parameter is function that returns boolean, second parameter is iterable
v = [1,9,-4,-8,10,3]
print(list(filter(lambda x: x>0, v)))

#customize sorted method using key=lambda
#sort the list of tuples by the y value, then x value
pts = [ (2,5), (12,3), (12,1), (6,5), (14, 10), (12, 10), \
          (8,12), (5,3) ]
print(sorted(pts, key=lambda p: (p[1],p[0]), reverse=True))

#list comprehension
L = [i for i in range(1, 10)]
print(L)
v = [1,9,-4,-8,10,3]
L2 = [i for i in v if i>0]
print(L2)
L3 = [(i,j) for i in range(1, 5) for j in range(1, 5)]
print(L3)