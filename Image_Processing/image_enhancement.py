# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:03:38 2019

@author: RUDRAJIT
"""


import cv2
#image enhancement using CLAHE
#Contrast limited advanced Histogram enhancing

#loading image
img=cv2.imread('gunshot.jpg')

#conversion to gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#creating clahe object
clahe=cv2.createCLAHE()

#enhancing image

enh_img=clahe.apply(gray)

#saving enhanced image
cv2.imwrite('enhanced_image.jpg',enh_img)
print("Done Enhancing")



