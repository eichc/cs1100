# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:13:48 2022

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
    s = s.lstrip('/')
    return (num1, num2, num3, s)

def get_line(fname, parno, lineno):
    f = open(fname, encoding='utf8')
    whole_file = f.read()
    paragraphs = whole_file.split('\n\n')
    p = paragraphs[parno-1]
    lines = p.split('\n')
    line = lines[lineno-1].rstrip()
    return line


fnum = input("Please enter the file number ==> ").strip()
fname = fnum + '.txt'
parno = int(input("Please enter the paragraph number ==> ").strip())
lineno = int(input("Please enter the line number ==> ").strip())

line = get_line(fname, parno, lineno)
new_file = open("output.txt", "w")
while line != 'END/0/0/0':
    clue = parse_line(line)
    new_file.write(clue[3] + '\n')
    line = get_line('{}.txt'.format(clue[0]), clue[1], clue[2])

new_file.close()