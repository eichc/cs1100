# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:58:45 2022

@author: eichc

Transforms a given phrase into a hashtag (no spaces, each word is capitalized)
and outputs the result.
"""

phrase = 'Things you wish you knew as a freshman'
hashtag = phrase.title()
hashtag = hashtag.replace(' ','')
hashtag = '#' + hashtag
print('The phrase "' + phrase + '"\nbecomes the hashtag "' + hashtag + '"')