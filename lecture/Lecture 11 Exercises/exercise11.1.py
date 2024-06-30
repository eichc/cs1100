# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:25:48 2022

@author: eichc
"""

def earlier_semester(first, second):
    flag = False
    if first[1] < second[1]:
        flag = True
    elif first[1] == second[1] and first[0] > second[0]:
        flag = True
    return flag

w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w1,w3)))