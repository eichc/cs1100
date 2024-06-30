# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:50:06 2022

@author: eichc
"""

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

print(get_line(fname, parno, lineno))