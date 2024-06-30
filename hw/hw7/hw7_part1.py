# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:56:28 2022

@author: Cam Eich

Basic autocorrect program. Take a list of words and find possible words in the
English dictionary to replace them with, by either inserting, deleting, or
replacing a letter.
"""

def drop_letter(word, dictionary):
    '''
    Given a word, find all possible ways to drop a single letter from the
    word. Return a set containing all of the possibilities that appear
    in the dictionary.
    '''
    replacements = set()
    w_list = list(word)
    for i in range(len(w_list)):
        temp = w_list.copy()
        temp.pop(i)
        new_word = ''.join(temp)
        if new_word in dictionary:
            replacements.add(new_word)
    return replacements

def insert_letter(word, dictionary):
    '''
    Given a word, find all possible ways to insert a single letter into the
    word. Return a set containing all of the possibilities that appear in the
    dictionary.
    '''
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    replacements = set()
    w_list = list(word)
    for i in range(len(w_list)+1):
        for j in range(len(abc)):
            temp = w_list.copy()
            temp.insert(i, abc[j])
            new_word = ''.join(temp)
            if new_word in dictionary:
                replacements.add(new_word)
    return replacements

def swap_letter(word, dictionary):
    '''
    Given a word, find all possible ways to swap two consecutive letters.
    Return a set containing all of the possibilities that appear in the
    dictionary.
    '''
    replacements = set()
    w_list = list(word)
    for i in range(len(w_list)-1):
        temp = w_list.copy()
        temp[i], temp[i+1] = temp[i+1], temp[i]
        new_word = ''.join(temp)
        if new_word in dictionary:
            replacements.add(new_word)
    return replacements

def replace_letter(word, dictionary, keyboard):
    '''
    Given a word, find all possible ways to replace a single letter given the
    possbile replacements described by keyboard. Return a set containing all
    of the possibilities that appear in the dictionary.
    '''
    replacements = set()
    w_list = list(word)
    for i in range(len(w_list)):
        for j in range(len(keyboard[w_list[i]])):
            temp = w_list.copy()
            temp.pop(i)
            temp.insert(i, keyboard[w_list[i]][j])
            new_word = ''.join(temp)
            if new_word in dictionary:
                replacements.add(new_word)
    return replacements

def common_replacements(replacements, dictionary):
    '''
    Given a set of possible replacements, return a list of the 3 most common
    in order of frequency.
    '''
    #create a list of sets containing each word and its frequency
    frequencies = []
    for word in replacements:
        frequencies.append((dictionary[word], word))
    frequencies.sort(reverse=True)
    #keep only the 3 most frequent words
    commons = []
    i = 0
    while i < min(3, len(replacements)):
        commons.append(frequencies[i][1])
        i += 1
    return commons


if __name__ == "__main__":
    #inputs and initialization
    dict_file = input("Dictionary file => ").strip()
    print(dict_file)
    
    in_file = input("Input file => ").strip()
    print(in_file)
    
    key_file = input("Keyboard file => ").strip()
    print(key_file)
    
    dictionary = dict()
    for line in open(dict_file):
        L = line.strip().split(',')
        word = L[0]
        freq = L[1]
        dictionary[word] = freq
    
    keyboard = dict()
    for line in open(key_file):
        L = line.strip().split()
        letter = L[0]
        replacements = list()
        for i in range(1, len(L)):
            replacements.append(L[i])
        keyboard[letter] = replacements
    
    
    #loop through input file
    for line in open(in_file):
        word = line.strip()
        #number of spaces to format the word to 15 characters
        num_spaces = 15 - len(word)
        
        #check if word is in dictionary
        if word in dictionary:
            print(' '*num_spaces + word + ' -> FOUND')
        else:
            #create a set with all possible replacements for the word
            replacements = set()
            for replacement in drop_letter(word, dictionary):
                replacements.add(replacement)
            for replacement in insert_letter(word, dictionary):
                replacements.add(replacement)
            for replacement in swap_letter(word, dictionary):
                replacements.add(replacement)
            for replacement in replace_letter(word, dictionary, keyboard):
                replacements.add(replacement)
            
            #find the 3 most common replacements, in order of frequency
            commons = common_replacements(replacements, dictionary)
            
            #check if there were any possible replacements, and if so print them
            if len(replacements) == 0:
                print(' '*num_spaces + word + ' -> NOT FOUND')
            else:
                print(' '*num_spaces + word + \
                      ' -> FOUND {:2d}: '.format(len(replacements)), end='')
                for i in range(len(commons)):
                    print(' ' + commons[i], end='')
                print()
            