# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:26:54 2019

@author: RUDRAJIT
"""
from PIL import Image

img=Image.open('test2.png')
rgb_im=img.convert('RGB')#convert image to rgb value
r,g,b=rgb_im.getpixel((101,1))#row column
print(r,g,b)


