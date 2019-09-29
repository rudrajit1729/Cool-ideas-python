# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:12:27 2019

@author: Rudrajit
"""


from PIL import Image
from random import randint
def check_ladder(points):
    ladderbeg=[8,21,43,50,54,62,66,80]
    ladderend=[26,82,77,91,93,96,87,100]
    if points in ladderbeg:
        print("Ladder!!!")
        return ladderend[ladderbeg.index(points)]
    else:
        return points
def check_snake(points):
    snakehead=[44,46,48,52,55,59,64,69,73,83,92,95,98]
    snaketail=[22,5,9,11,7,17,36,33,1,19,51,24,28]
    if points in snakehead:
        print("Snake :(")
        return snaketail[snakehead.index(points)]
    else:
        return points
def show_board():
    img=Image.open("slb.jpg")
    img.show()
def play():
    p1name=input("Enter name player 1:")
    p2name=input("Enter name player 2:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1name,"your turn")
            c=int(input("Press 1 to continue 0 to quit:"))
            if c==0:
                print(p1name,"scored",pp1)
                print(p2name,"scored",pp2)
                print("Quitting game...\nThanks for playing")
                break
            dice=randint(1,7)
            print("Dice showed:",dice)
            pp1+=dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>=100:
                print(p1name,"won!!!")
                exit()
        else:
            print(p2name,"your turn")
            c=int(input("Press 1 to continue 0 to quit:"))
            if c==0:
                print(p1name,"scored",pp1)
                print(p2name,"scored",pp2)
                print("Quitting game...\nThanks for playing")
                break
            dice=randint(1,7)
            print("Dice showed:",dice)
            pp2+=dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>=100:
                print(p1name,"won!!!")
                exit()
        turn+=1
show_board()
play()