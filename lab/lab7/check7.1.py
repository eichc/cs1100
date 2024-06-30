# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:31:32 2022

@author: eichc
"""

def parse_line(line):
    if line.count('/') < 3:
        return
    L = line.split('/')
    if not(L[-1].isnumeric() and L[-2].isnumeric() and L[-3].isnumeric()):
        return
    num1 = int(L[-3])
    num2 = int(L[-2])
    num3 = int(L[-1])
    s = ''
    for i in range(len(L) - 3):
        s = '/'.join([s, L[i]])
    return (num1, num2, num3, s)

print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
