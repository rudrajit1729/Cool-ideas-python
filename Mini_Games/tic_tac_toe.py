# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])

def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            return True
    return False

def check_diag(symbol):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board [1][1]==symbol:
        return True
    if board[1][1]==board[0][2] and board[0][2]==board[2][0] and board[1][1]==symbol:
        return True
    return False

def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diag(symbol)

def place(symbol):
    print(np.matrix(board))
    while(1):
        row=int(input("Enter row (1 or 2 or 3):"))
        column=int(input("Enter column(1 or 2 or 3):"))
        if row>0 and row <4 and column >0 and column <4 and board[row-1][column-1]=='-':
            break
        else:
            print("Invalid input.Please enter again")
    board[row-1][column-1]=symbol
def play():
    p1s='X'
    p2s='O'
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1s)
            if won(p1s):
                print("X won")
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                print("0 won")
                break
    if not (won(p1s) or won(p2s)):
        print("Draw")
play()
