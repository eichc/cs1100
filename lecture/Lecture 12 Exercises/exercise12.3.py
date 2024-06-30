# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:26:48 2022

@author: eichc
"""

def find_min(L):
    minimum = L[0][0]
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] < minimum:
                minimum = L[i][j]
    return minimum

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )