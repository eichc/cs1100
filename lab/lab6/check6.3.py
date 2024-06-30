# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:33:46 2022

@author: eichc
"""

import lab06_util

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

def verify_board(board):
    #ensure no empty spaces
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return False
            
    #ensure no incorrect numbers
    for i in range(9):
        for j in range(9):
            if not ok_to_add(board, i, j, int(board[i][j])):
                return False
    return True
    

file_name = input("Enter file name: ")
board = lab06_util.read_sudoku(file_name)

while not verify_board(board):
    row = int(input("Enter a row: "))
    col = int(input("Enter a column: "))
    number = int(input("Enter a number: "))
    
    if ok_to_add(board, row, col, number):
        board[row][col] = number
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('-'*25)
            for j in range(9):
                if j % 3 == 0:
                    print('| ', end='')
                print(board[i][j], end=' ')
            print('|')
    else:
        print("This number cannot be added")