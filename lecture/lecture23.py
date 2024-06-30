# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:30:21 2022

@author: eichc
"""

def blast(n):
    if n>0:
        print(n)
        blast(n-1)
    else:
        print("Blast off!")

# blast(5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# print(fib(5))

def flatten(L):
    result = []
    for x in L:
        if type(x) == list:
            result.extend( flatten(x) )
        else:
            result.append(x)
    return result

# v = [[1,5], 6, [[2]], [3, [7, 8, [9,10], [11,12] ]]]
# print(v)
# print(flatten(v))

def merge(L1, L2):
    """ 
    Assume L1 and L2 are sorted. Create a new list L that is the merged
    version of L1&L2.
    """
    L = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            val = L1[i]
            L.append( val )
            i += 1
        else:
            val = L2[j]
            L.append( val )
            j += 1
    ## at this point, either L1 or L2 has run out of values
    ## add all the remaining values to the end of L.
    L.extend(L1[i:]) 
    L.extend(L2[j:])
    return L

def merge_sort(L):
    if len(L) == 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)