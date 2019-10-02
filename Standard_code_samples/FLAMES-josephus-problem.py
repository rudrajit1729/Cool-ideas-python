# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:29:05 2019

@author: RUDRAJIT
"""

p1=list(input("Enter person 1 name:").lower())
p2=list(input("Enter person 2 name:").lower())

def remove_match(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                l1.pop(i)
                l2.pop(j)
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]

while(True):
    ret_list=remove_match(p1,p2)
    if ret_list[1]==False:
        break
    c=ret_list[0].index("*")#index of * marker
    p1=ret_list[0][:c]
    p2=ret_list[0][c+1:]
    
star_ind=ret_list[0].index("*")
p1=ret_list[0][:star_ind]
p2=ret_list[0][star_ind+1:]
count=len(p1)+len(p2)
result=["Friends","Love","Affection","Marriage","Enemy","Siblings"]
while len(result)>1:
    split_index=(count%len(result))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
print(result[0])



