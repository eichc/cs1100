# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:00:47 2022

@author: eichc
"""

#sets don't allow duplicates
#there are no indices in sets - essentially just a bag of values
s1 = set([1,1,1,2,4,5,3,5])
# print(s1)

#sets are not actually sorted even though it may look like it
s2 = set([5,4,'bee',3,'apple'])
# print(s2)

#add() adds the value to the set, not necessarily to the end
s2.add(8)
# print(s2)

#clear() removes all values from the set
# s1.clear()
# print(s1)

#union creates a new set with all values in either set
# print(s1 | s2)
s3 = s1.union(s2)
# print(s3)

#intersection creates a new set with only values that are in both sets
# print(s1 & s2)
s3 = s1.intersection(s2)
# print(s3)

#difference creates a new set with values from the first set that aren't in the second set
# print(s1 - s2)
s3 = s1.difference(s2)
# print(s3)

#symmetric_difference() is essentially exclusive or, also denoted with ^
# print(s1 ^ s2)
s3 = s1.symmetric_difference(s2)
# print(s3)

#issubset() checks if all values of the first set appear in the second set
#issuperset() checks if all values of the second appear in the first
#can also use <= and >=, respectively


#Big O Notation:
    #theoretical complexity of the code
    #O(size of input)^N
    #for the list solution: O(N^2)
    #for the set solution: O(N)