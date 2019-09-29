# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:26:22 2019

@author: Rudrajit
"""
import turtle
from random import randint
turtle.bgcolor("black")
tur=turtle.Turtle()
dot_dist=25
tur.setpos(-250,250)
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]
tur.penup()


def spiral(m,n):#m=rows n=columns a=matrix
    k,l,f=0,0,0
    '''
    k=index of starting row
    l=index of starting column
    f=flag for checking direction change condition
    m-ending row index
    n=ending column index
    '''
    col=randint(0,10)
    tur.color("blue")

    while(k<m and l<n):

        if(f==1):
            tur.right(90)
        
        #printing the first row out of remaining rows
        for i in range(l,n):
            #print(a[k][i],end=" ")
            tur.dot()
            tur.forward(dot_dist)
        k+=1
        f=1
        
        tur.right(90)
        col=randint(0,10)
        tur.color(list_color[col])
        #printing the last column out of remaining columns
        for i in range(k,m):
            #print(a[i][n-1],end=" ")
            tur.dot()
            tur.forward(dot_dist)
        n-=1
        tur.right(90)
        col=randint(0,10)
        tur.color(list_color[col])

        if(k<m):#checking the condition again as k has been increamented
            #printing the last row out of remaining rows
            for i in range(n-1,l-1,-1):#we wanna include l inex as well
                tur.dot()
                tur.forward(dot_dist)
                #print(a[m-1][i],end=" ")
            m-=1
        tur.right(90)
        col=randint(0,10)
        tur.color(list_color[col])

        if (l<n):#checking the condition again as l has been increamented
            #printing the first column out of remaining columns
            for i in range(m-1,k-1,-1):#we wanna include k index as well
                tur.dot()
                tur.forward(dot_dist)
                #print(a[i][l],end=" ")
            l+=1
        

spiral(20,20)
turtle.done()
'''penup function makes turtle write nothing unless dot func or any other
writing fun is called specifically thus stops it from printing random lines'''






