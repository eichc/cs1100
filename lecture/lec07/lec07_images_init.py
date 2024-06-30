# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:01:19 2022

@author: eichc
"""

from PIL import Image

filename = "chipmunk.jpg"
im = Image.open(filename)
print('\n' '********************')
print("Here's the information about", filename)
print(im.format, im.size, im.mode)

gray_im = im.convert('L')
scaled = gray_im.resize( (128,128) )
print("After converting to gray scale and resizing,")
print("the image information has changed to")
print(scaled.format, scaled.size, scaled.mode)

scaled.show()
scaled.save(filename + "_scaled.jpg")