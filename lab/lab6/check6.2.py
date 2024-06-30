# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:09:31 2022

@author: eichc
"""

def ok_to_add(bd, r, c, n):
    temp = bd[r][c]
    bd[r][c] = '.'
    
    #check if the location and number are valid
    if not(0 <= r <= 8 and 0 <= c <= 8 and 1 <= n <= 9):
        return False
    
    #check row
    for i in range(9):
        if bd[r][i] == str(n):
            bd[r][c] = temp
            return False
    #check column
    for i in range(9):
        if bd[i][c] == str(n):
            bd[r][c] = temp
            return False
    #check block
    for i in range((r//3)*3, (r//3)*3 + 3):
        for j in range((c//3)*3, (c//3)*3 + 3):
            if bd[i][j] == str(n):
                bd[r][c] = temp
                return False
    return True


bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

#print the board
for i in range(9):
    if i % 3 == 0 and i != 0:
        print('-'*25)
    for j in range(9):
        if j % 3 == 0:
            print('| ', end='')
        print(bd[i][j], end=' ')
    print('|')
    

row = int(input("Enter a row: "))
col = int(input("Enter a column: "))
number = int(input("Enter a number: "))

if ok_to_add(bd, row, col, number):
    bd[row][col] = number
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-'*25)
        for j in range(9):
            if j % 3 == 0:
                print('| ', end='')
            print(bd[i][j], end=' ')
        print('|')
else:
    print("This number cannot be added")





