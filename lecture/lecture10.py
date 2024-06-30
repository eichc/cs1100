# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:52:04 2022

@author: eichc
"""

# #aliasing happens when passed to functions, to avoid make a new list at start of function
def smallest_two(mylist):
      mylist.sort()
      newlist = []
      if len(mylist) > 0:
          newlist.append(mylist[0])
          if len(mylist) > 1:
              newlist.append(mylist[1])
      return newlist

values = [35, 34, 20, 40, 60, 30]

print("Before function:", values)
print("Result of function:", smallest_two(values))
print("After function:", values)


# #for loop example
# animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
# cap_animals = []
# for animal in animals:
#     cap_animals.append( animal.capitalize() )
# print(cap_animals)


# #prints indeces of each element of animals
# animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
# for i in range(len(animals)):
#     print(i)


# #slicing
# co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
#   348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
# three_values = co2_levels[2:5]
# print(three_values)


# #Strings to Lists
# s = "Hello world"
# t = list(s)
# print(t)
# print(s.split())


#Lists to Strings - all elements of the list must be a string
# L1 = [ 'No', 'one', 'expects', 'the', 'Spanish', 'Inquisition' ]
# print(''.join(L1))
# print(' '.join(L1))