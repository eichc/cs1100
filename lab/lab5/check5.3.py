# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:31:54 2022

@author: eichc
"""

import lab05_util
import webbrowser

def get_avg(nums):
    total = sum(nums)
    if len(nums) > 3:
        total -= max(nums)
        total -= min(nums)
        avg = total / (len(nums)-2)
    else:
        avg = total / len(nums)
    return avg

def print_info(restaurant):
    address = restaurant[3].split('+')
    score = get_avg(restaurant[-1])
    
    #print the info
    print(restaurant[0], "({})".format(restaurant[5]))
    for line in address:
        print("\t" + line)
    
    #print reviews
    if score < 2:
        print("This restaurant is rated bad, based on", len(restaurant[-1]),
              "reviews.")
    elif score < 3:
        print("This restaurant is rated average, based on", len(restaurant[-1]),
              "reviews.")
    elif score < 4:
        print("This restaurant is rated above average, based on", 
              len(restaurant[-1]), "reviews.")
    else:
        print("This restaurant is rated very good, based on", len(restaurant[-1]),
              "reviews.")
        

#main code
restaurants = lab05_util.read_yelp('yelp.txt')

#print the info of the chosen restaurant
id_num = int(input("Enter restaurant id: "))
if id_num < 1 or id_num > len(restaurants):
    print("Warning: Restaurant {} does not exist.".format(id_num))
else:
    print_info(restaurants[id_num-1])

    #browse the web for the chosen restaurant
    print("What would you like to do next?")
    print("1. Visit the homepage")
    print("2. Show on Google Maps")
    print("3. Show directions to this restaurant")
    choice = int(input("Your choice (1-3) ==> "))
    
    if choice == 1:
        webbrowser.open(restaurants[id_num-1][4])
    elif choice == 2:
        webbrowser.open('http://www.google.com/maps/place/' + restaurants[id_num-1][3])
    elif choice == 3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/' + restaurants[id_num-1][3])





