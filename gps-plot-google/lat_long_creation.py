# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:25:59 2019

@author: HP
"""


import csv
from random import randint

with open("route.csv",'a') as f:
    for i in range(25):
        lat=str(28.689)+str(randint(500,890))
        long=str(77.323)+str(randint(500,890))
        f.write("\n{0},{1}".format(lat,long))
f.close()

with open("route.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        print(lat)
        print(long)
        print()
f.close()