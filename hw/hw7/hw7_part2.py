# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:54:45 2022

@author: Cam Eich

Given movies and ratings from IMDB and Twitter, tell the user the best and
worst movie from a chosen range of years, from a chosen genre. The quality
of each movie is a combination of the IMDB and Twitter ratings.
"""

import json

def find_movies(y1, y2, movies):
    '''
    Find all of the movies made between y1 and y2 (inclusive). Return them in 
    a dictionary.
    '''
    new_movies = dict()
    for movie in movies:
        year = movies[movie]['movie_year']
        if y1 <= year <= y2:
            new_movies[movie] = movies[movie]
    return new_movies

def comb_rating(movies, twitter, w1, w2):
    '''
    Calculate the combined rating of each movie in movies, based on its IMDB
    rating and average Twitter rating. IMDB rating's weight is w1, and
    Twitter's is w2. Return a copy of the movies dictionary, with the combined
    ratings added to the end of each entry.
    '''
    ratings = dict()
    for movie in movies:
        if (movie in twitter) and len(twitter[movie]) >= 3:
            twt_rating = sum(twitter[movie]) / len(twitter[movie])
            imdb_rating = movies[movie]['rating']
            rating = (w1 * imdb_rating + w2 * twt_rating) / (w1 + w2)
            ratings[movie] = movies[movie]
            ratings[movie]['comb_rating'] = rating
    return ratings

def find_genre(genre, movies):
    '''
    Find all movies with the specified genre, and return them in a dictionary.
    '''
    genre = genre.title()
    new_movies = dict()
    for movie in movies:
        genres = movies[movie]['genre']
        if genre in genres:
            new_movies[movie] = movies[movie]
    return new_movies

def movie_info(movies):
    '''
    Return a list of tuples containing the movie name, year, and rating. The
    list is sorted first by rating, then by name as a tie-breaker.
    '''
    info = []
    for movie in movies:
        rating = movies[movie]['comb_rating']
        name = movies[movie]['name']
        year = movies[movie]['movie_year']
        info.append((rating, name, year))
    info.sort(reverse=True)
    return info
    

if __name__ == "__main__":
    #initialization and inputs
    movies = json.loads(open("movies.json").read())
    twitter = json.loads(open("ratings.json").read())
    
    min_year = input("Min year => ").strip()
    print(min_year)
    min_year = int(min_year)
    
    max_year = input("Max year => ").strip()
    print(max_year)
    max_year = int(max_year)
    
    imdb_w = input("Weight for IMDB => ").strip()
    print(imdb_w)
    imdb_w = float(imdb_w)
    
    twt_w = input("Weight for Twitter => ").strip()
    print(twt_w)
    twt_w = float(twt_w)
    
    
    #restrict the movies dictionary to only movies within the year range
    restricted_movies = find_movies(min_year, max_year, movies)
   
    #start the loop of asking for genre and finding highest & lowest rated movie
    print()
    genre = input("What genre do you want to see? ").strip()
    print(genre)
    
    while genre.lower() != 'stop':
        #find all movies within specified genre
        genre_movies = find_genre(genre, restricted_movies)
        
        #find the combined ratings of each movie
        comb_ratings = comb_rating(genre_movies, twitter, imdb_w, twt_w)
        
        #get the rating, name, and year of each movie, sorted from highest
        #rating to lowest
        info = movie_info(comb_ratings)
        
        #determne if any movies were found
        print()
        if len(comb_ratings) == 0:
            print("No {} movie found in {} through {}".format(genre.title(), 
                                                              min_year, max_year))
        else:
            best = info[0]
            print("Best:")
            print("        Released in {}, {} has a rating of {:.2f}".format(best[2],
                                                                  best[1], best[0]))
            print()
            worst = info[-1]
            print("Worst:")
            print("        Released in {}, {} has a rating of {:.2f}".format(worst[2],
                                                                  worst[1], worst[0]))
        
        print()
        genre = input("What genre do you want to see? ").strip()
        print(genre)
    