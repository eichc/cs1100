# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:42:58 2022

@author: eichc

Determine the sentiment of a given sentence (happy, sad, or neutral).
"""

def number_happy(sentence):
    '''
    Return the number of happy words in a sentence.
    '''
    sentence = sentence.lower()
    count = 0
    count += sentence.count("laugh")
    count += sentence.count("happiness")
    count += sentence.count("love")
    count += sentence.count("excellent")
    count += sentence.count("good")
    count += sentence.count("smile")
    return count
    
def number_sad(sentence):
    '''
    Return the number of sad words in a sentence.
    '''
    sentence = sentence.lower()
    count = 0
    count += sentence.count("bad")
    count += sentence.count("sad")
    count += sentence.count("terrible")
    count += sentence.count("horrible")
    count += sentence.count("problem")
    count += sentence.count("hate")
    return count

if __name__ == "__main__":
    sentence = input("Enter a sentence => ").strip()
    print(sentence)

    #Calculate and print the sentiment
    happySent = number_happy(sentence)
    sadSent = number_sad(sentence)
    print("Sentiment: " + "+"*happySent + "-"*sadSent)

    #Determine if the sentence is happy, sad, or neutral
    if happySent > sadSent:
        print("This is a happy sentence.")
    elif happySent < sadSent:
        print("This is a sad sentence.")
    else:
        print("This is a neutral sentence.")