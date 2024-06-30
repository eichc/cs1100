# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:00:51 2022

@author: Cam Eich

Given a password, determine its score and rating based on criteria such as
its length, number of uppercase and lowercase letters, number of digits,
number of punctuation symbols, if it could match a NY license plate, and if it
appears on a list of common passwords.
"""

import hw4_util

def len_score(password):
    '''
    Given a password, calculate how the password's length affects its score.
    If there is a net change in the score, tell the user. Return the change in
    score.
    '''
    score = 0
    if len(password) == 6 or len(password) == 7:
        score = 1
    elif 8<= len(password) <= 10:
        score = 2
    elif len(password) > 10:
        score = 3
    if score > 0:
        print("Length: +{}".format(score))
    return score

def case_score(password):
    '''
    Given a password, calculate how the amount of uppercase and lowercase letters
    affects the score. If there is a net change in the score, tell the user.
    Return the change in score.
    '''
    score = 0
    upper = 0
    lower = 0
    #count number of uppercase and lowercase
    for letter in password:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    if upper >= 2 and lower >= 2:
        score = 2
    elif upper >= 1 and lower >= 1:
        score = 1
    if score > 0:
        print("Cases: +{}".format(score))
    return score

def digits_score(password):
    '''
    Given a password, calculate how the number of digits affects the score. If
    there is a net change in the score, tell the user. Return the change in score.
    '''
    score = 0
    digits = 0
    for i in range(10):
        digits += password.count(str(i))
    if digits >= 2:
        score = 2
    elif digits == 1:
        score = 1
    if score > 0:
        print("Digits: +{}".format(score))
    return score

def punct_score(password):
    '''
    Given a password, calculate how the number of punctuation symbols affects
    the score. If there is a net change in the score, tell the user. Return
    the change in score.
    '''
    score = 0
    flag1 = False
    flag2 = False
    punct1 = ['!', '@', '#', '$']
    punct2 = ['%', '^', '&', '*']
    
    #determine if the symbols from either list appear in the password
    for symbol in punct1:
        if password.count(symbol) > 0:
            flag1 = True
    for symbol in punct2:
        if password.count(symbol) > 0:
            flag2 = True
    
    #calculate and print change in score
    if flag1:
        score += 1
        print("!@#$: +1")
    if flag2:
        score += 1
        print("%^&*: +1")
    return score

def lic_score(password):
    '''
    Determine if a password could match a NY license plate, and subtract from
    the score if it does. If there is a net change in the score, tell the user.
    Return the change in score.
    '''
    password = password.lower()
    if len(password) < 7:
        return 0
    for i in range(len(password)-6):
        #determine if there are 3 consecutive letters
        if password[i].isalpha() and password[i+1].isalpha() and \
            password[i+2].isalpha():
            #determine if the next 4 characters are numbers
            flag = True
            for j in range(i+3, i+7):
                if not password[j].isnumeric():
                    flag = False
            if flag:
                print("License: -2")
                return -2
    return 0
            
def common_score(password):
    '''
    Determine if the password is found on a list of common passwords, and
    subtract from the score if it does. If there is a net change in the score,
    tell the user. Return the change in score.
    '''
    commons = hw4_util.part1_get_top()
    password = password.lower()
    for word in commons:
        if word == password:
            print("Common: -3")
            return -3
    return 0

    
if __name__ == "__main__":
    #input password
    password = input("Enter a password => ").strip()
    print(password)
    
    #calculate the score
    score = 0
    score += len_score(password)
    score += case_score(password)
    score += digits_score(password)
    score += punct_score(password)
    score += lic_score(password)
    score += common_score(password)
    
    print("Combined score:", score)
    
    #determine the rating
    if score <= 0:
        print("Password is rejected")
    elif score <= 2:
        print("Password is poor")
    elif score <= 4:
        print("Password is fair")
    elif score <= 6:
        print("Password is good")
    else:
        print("Password is excellent")






