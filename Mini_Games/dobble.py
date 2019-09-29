# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:49:59 2019

@author: HP
"""

#dobble
#8 characters on each card
import string
import random
s=list(string.ascii_uppercase)
card1=[]
length=5
card2=[]
for i in range(length):
    item=random.choice(s)
    card1.append(item)
    s.remove(item)
    item=random.choice(s)
    card2.append(item)
    s.remove(item)
item=random.choice(s)
pos1=random.randint(0,length-1)
pos2=random.randint(0,length-1)
card1.pop(pos1)
card2.pop(pos2)
card1.insert(pos1,item)
card2.insert(pos2,item)
print(card1)
print(card2)
ch=input("enter the common element")
if ch==item:
    print("right")
else:
    print("wrong")






