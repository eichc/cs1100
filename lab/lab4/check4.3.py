# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:24:15 2022

@author: eichc
"""

from PIL import Image

im = Image.new('RGB', (1000, 360), 'white')

#import the 6 images
im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')
im6 = Image.open('6.jpg')

#resize the images
im1 = im1.resize((256 * im1.size[0] // im1.size[1], 256))
im2 = im2.resize((256 * im2.size[0] // im2.size[1], 256))
im3 = im3.resize((256 * im3.size[0] // im3.size[1], 256))
im4 = im4.resize((256 * im4.size[0] // im4.size[1], 256))
im5 = im5.resize((256 * im5.size[0] // im5.size[1], 256))
im6 = im6.resize((256 * im6.size[0] // im6.size[1], 256))

#paste the images onto the wallpaper
im.paste(im1, (31, 20))
im.paste(im2, (41 + im1.size[0], 60))
im.paste(im3, (51 + im1.size[0] + im2.size[0], 20))
im.paste(im4, (61 + im1.size[0] + im2.size[0] + im3.size[0], 60))
im.paste(im5, (71 + im1.size[0] + im2.size[0] + im3.size[0] + im4.size[0], 20))
im.paste(im6, (81 + im1.size[0] + im2.size[0] + im3.size[0] + im4.size[0] + 
               im5.size[0], 60))

im.show()