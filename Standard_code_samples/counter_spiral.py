# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:29:09 2019

@author: HP
"""
print("Enter dimension:")
n=int(input())
mat=[]
print("Enter elements")
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)
    
top=0
bot=n-1
lft=0
ri8=n-1
k=0
i,j=0,0
while(k<n*n-1):
        
    print(mat[i][j],end=" ")
    k+=1
    if(j==lft and i<bot):
        i+=1
    elif(i==bot and j<ri8):
        j+=1
    elif (j==ri8 and i>top):
        i-=1
    elif (i==top and j>lft):
        j-=1
    if (i==top and j==lft):
        top+=1
        bot-=1
        lft+=1
        ri8-=1
        i=top
        j=lft
print(mat[i][j],end="")       
    
    
        