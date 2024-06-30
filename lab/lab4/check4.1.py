# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:47:22 2022

@author: eichc
"""

from PIL import Image

im = Image.new('RGB', (512, 512), 'white')

#import the 4 images
im1 = Image.open('ca.jpg')
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')

#resize the images
im1 = im1.resize((256, 256))
im2 = im2.resize((256, 256))
im3 = im3.resize((256, 256))
im4 = im4.resize((256, 256))

#paste the images on the blank wallpaper
im.paste(im1, (0, 0))
im.paste(im2, (0, 256))
im.paste(im3, (256, 0))
im.paste(im4, (256, 256))

im.show()