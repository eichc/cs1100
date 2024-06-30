# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:40:54 2022

@author: eichc
"""

imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)

max_actors = 0
max_movie = ''
singles = 0
for movie in movies:
    if len(movies[movie]) > max_actors:
        max_actors = len(movies[movie])
        max_movie = movie
    if len(movies[movie]) == 1:
        singles += 1
print(max_actors)
print(max_movie)
print(singles)