# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:08:16 2019

@author: RUDRAJIT
"""

from PIL import Image
from random import randint
img=Image.open("map.png")
rgb_img=img.convert("RGB")
#dimensions 3818x4600
count_wb=0
count=0
count_ind=0
while(count<=10000):
    y=randint(0,4599)
    x=randint(0,3817)
    r,g,b=rgb_img.getpixel((x,y))
    #colours black(0,0,0) grey(204,236,230)
    if r==0:
        count_ind+=1
        count+=1
    else:
        if r==204:
            count_wb+=1
            count+=1
            
area_ind=3287263
area_act_wb=88752
area_wb=(area_ind*count_wb)/count_ind
print("Actual area={0}\nPredicted area={1}".format(area_act_wb,area_wb))
