# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:49:51 2022

@author: Cam Eich

Read in a paragraph of English sentences. Calculate average sentence length,
average number of syllables, percentage of hard words, and overall reading
difficulty.

"""
import syllables

def isHardWord(word):
    '''
    Determine if a word is a "hard word". Takes in a word as a string,
    returns a boolean.
    '''
    flag = False
    end = word[len(word)-2:] #last 2 letters of the word
    if syllables.find_num_syllables(word) >= 3 and word.count("-") == 0:
        flag = True
    if syllables.find_num_syllables(word) == 3:
        if end != 'es' and word != 'ed':
            flag = True
    return flag


if __name__ == "__main__":
    #input
    paragraph = input("Enter a paragraph => ").strip()
    print(paragraph)
    paragraph = paragraph.split()
    
    
    #calculate ASL
    totalWords = len(paragraph)
    sentences = 0
    for word in paragraph:
        if word.count(".") > 0:
            sentences += 1
    ASL = totalWords / sentences
    
    
    #calculate PHW
    phwList = []
    numHardWords = 0
    for word in paragraph:
        if isHardWord(word):
            phwList.append(word)
            numHardWords += 1
    PHW = numHardWords / totalWords * 100
    
    
    #calculate ASYL
    totalSyllables = 0
    for word in paragraph:
        totalSyllables += syllables.find_num_syllables(word)
    ASYL = totalSyllables / totalWords
    
    
    #calculate GFRI and FKRI
    GFRI = 0.4*(ASL + PHW)
    FKRI = 206.835 - 1.015*ASL - 86.4*ASYL
    
    
    #print the output
    print("Here are the hard words in this paragraph:")
    print(phwList)
    print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL, PHW, ASYL))
    print("Readability index (GFRI): {:.2f}".format(GFRI))
    print("Readability index (FKRI): {:.2f}".format(FKRI))
    









