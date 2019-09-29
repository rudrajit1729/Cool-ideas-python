# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 09:36:47 2019

@author: RUDRAJIT
"""

import scipy.misc
from PIL import Image
import random
import numpy as np

img=scipy.misc.imread("map.png")
count_wb=0
count_ind=0
count=0

while(count<=10000):
    #dimension 3818x4600
    x=random.randint(0,4599)
    y=random.randint(0,3817)
    z=0
    #colour black(0,0,0) grey(204,236,230)
    if (img[x][y][z]==0):
        count_ind+=1
        count+=1
    else:
        if(img[x][y][z]==204):
            count_wb+=1
            count+=1
area_ind=3287263
area_act_wb=88752
area_wb=(area_ind*count_wb)/count_ind
print("Actual area={0}\nPredicted area={1}".format(area_act_wb,area_wb))
