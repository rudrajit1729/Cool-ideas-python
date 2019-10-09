# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:17:01 2019

@author: RUDRAJIT
"""
import numpy as np
from PIL import Image
im=Image.open("lena.jpg")
pixelMap=im.load()
I=np.asanyarray(Image.open("lena.jpg"))#seeing image as matrix
img=Image.new(im.mode,im.size)
pixelNew=img.load()

'''
2^8->2^3
Divide by 2^5
0-31=0
32-63=1
...
224-255=7
'''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixelMap[i,j]>=0 and pixelMap[i,j]<=31):
            pixelNew[i,j]=0
        elif (pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelNew[i,j]=1
        elif (pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelNew[i,j]=2
        elif (pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelNew[i,j]=3
        elif (pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
            pixelNew[i,j]=4
        elif (pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
            pixelNew[i,j]=5
        elif (pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
            pixelNew[i,j]=6
        elif (pixelMap[i,j]>=224 and pixelMap[i,j]<=255):
            pixelNew[i,j]=7
img.save("lena_comp.jpg")
J=np.asanyarray(Image.open("lena_comp.jpg"))