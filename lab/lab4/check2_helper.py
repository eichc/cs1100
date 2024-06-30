# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:01:14 2022

@author: eichc
"""
from PIL import Image

def make_square(image):
    width, height = image.size
    if width > height:
        image = image.crop((0, 0, height, height))
    else:
        image = image.crop((0, 0, width, width))
    return image