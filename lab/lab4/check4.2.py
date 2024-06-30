# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:01:30 2022

@author: eichc
"""

from PIL import Image
import check2_helper as helper

im = Image.new('RGB', (512, 512), 'white')

#import the 4 images
im1 = Image.open('ca.jpg')
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')

#make the images square
im1 = helper.make_square(im1)
im2 = helper.make_square(im2)
im3 = helper.make_square(im3)
im4 = helper.make_square(im4)

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