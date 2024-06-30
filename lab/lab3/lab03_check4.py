# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:45:38 2022

@author: eichc

Calculate the future populations of bunnies and foxes.
"""
import math

#functions
def nextBpop(bpop, fpop):
    bpop_next = (10*bpop)/(1+0.1*bpop)- 0.05*bpop*fpop
    bpop_next = math.floor(bpop_next)
    return max(0, bpop_next)
    
def nextFpop(bpop, fpop):
    fpop_next = 0.4 * fpop + 0.02 * fpop * bpop
    fpop_next = math.floor(fpop_next)
    return max(0, fpop_next)


#inputs
bpop = int(input("Number of bunnies ==> "))
print(bpop)

fpop = int(input("Number of foxes ==> "))
print(fpop)


#print 5 years
i = 0
while i < 5:
    print("Year {}: {} {}".format(i + 1, bpop, fpop))
    newBpop = nextBpop(bpop, fpop)
    newFpop = nextFpop(bpop, fpop)
    bpop = newBpop
    fpop = newFpop
    i+=1