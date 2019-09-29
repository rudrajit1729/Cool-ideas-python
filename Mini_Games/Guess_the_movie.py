# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:35:34 2019

@author: HP
"""

#Guess the movie
#encorporate guess at once
#correct the s string
import random
movies=['golmaal','singham','interstellar','krrish','drishyam','mission mangal','bharat','zero','sultan','jungle book']

def create_qn(ans):
    qn='*'*len(ans)
    for i in range(len(ans)):
        if ans[i]==' ':
            qn=qn[0:i]+" "+qn[i+1:]
    print(qn)
    return qn

def unlock(ans,qn,c):
    qn=list(qn)
    ans=list(ans)
    qn2=''
    if c in ans:
        for i in range(len(ans)):
           if c==ans[i]:
               qn.pop(i)
               qn.insert(i,c)
    for i in qn:
        qn2+=i
    return qn2
    
def guess(movie):
    tries=0
    s=create_qn(movie)
    while tries<10:
        print("Guess The movie:",s)
        c=input("Input character:")
        if c in movie:
            print("Character present!!!")
            s=unlock(movie,s,c)
            if s==movie:
                return tries
            d=int(input("Press 1 to guess the movie 2 to unlock another letter"))
            if d==1:
                ans=input("Enter the movie:")
                if ans==movie:
                    print("Correct")
                    return tries
                else:
                    print("Try again")
                    tries+=1
            else:
                pass
                
            
        
        else:
            print("Character not present!!!")
            tries+=1
    return tries

def play():
    p1name=input("Player 1 enter name:")
    p2name=input("Player 2 enter name:")
    pp1=0
    pp2=0
    run=True
    turn=1
    while(run):
        if turn%2==0:
            print("Your turn",p1name,":")
            picked_movie=random.choice(movies)
            tries=guess(picked_movie)
            if tries==10:
                print("Correct answer:",picked_movie)
            pp1+=(10-tries)
            print(p1name," your Score:",pp1)
        else:
            print("Your turn",p2name,":")
            picked_movie=random.choice(movies)
            tries=guess(picked_movie)
            if tries==10:
                print("Correct answer:",picked_movie)
            pp2+=(10-tries)
            print(p2name," your Score:",pp2)
        ch=input("Enter y to continue")
        if ch!='y':
            run=False
        turn+=1
    print("Final scores:")
    print(p1name,":",pp1)
    print(p2name,":",pp2)

        
play()
            
        

        
    

        
        
    
