# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 11:04:38 2019

@author: HP
"""

#maximum numeric value from string
s=input()
alpha=[chr(x) for x in range(97,123)]
numbers=[]
for i in s:
    if i in alpha:
        s=s.replace(i,",")
l=list(s.split(","))
l2=[]
for i in l:
    if not(i==""):
        l2.append(i)
l2=[int(x) for x in l2]
print(max(l2))

