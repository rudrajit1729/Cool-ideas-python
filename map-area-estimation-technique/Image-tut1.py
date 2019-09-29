# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:12:06 2019

@author: RUDRAJIT
"""
import numpy as np
from PIL import Image

width=5
height=4

array=np.zeros([height,width,3],dtype=np.uint8)
img=Image.fromarray(array)
img.save("test.png")

array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0]#orange
array1[:,100:]=[0,0,255]#blue
img=Image.fromarray(array1)
img.save("test2.png")