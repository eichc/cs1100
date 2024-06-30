# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:00:05 2022

@author: eichc
"""

#loop over dictionary
# d2 = {'Gru': set([123, 456]), 'Margo': set([456])}
# for i in d2:
#     key = i
#     value = d2[i]
#     print(key, value)

#aliasing
# d = dict()
# d[15] = 'hi'
# L = []
# L.append(d)
# d[20] = 'bye'
# L.append(d.copy())
# d[15] = 'hello'
# del d[20]
# print(L)

#who appeared in the most (unique) movies?
imdb_file = input("Enter the name of the IMDB file ==> ").strip()
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)
max_num = 0
max_name = ''
for actor in movies:
    if len(movies[actor]) > max_num:
        max_num = len(movies[actor])
        max_name = actor
print("{} appeared in {} movies".format(max_name, max_num))
print(movies['Bacon, Kevin'])