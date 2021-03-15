
from terminal_tic_tac_toe import *


board = genBoard()
pl1, pl2 = ['a1', 'b2'], ['b1', 'c1']



def Mmax(board, score, pl1, pl2, ):
    score = 0
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            #print(square)##
            pl1.append(square)
            if checkWin(pl1) == 'win':
                score = 1
                #print(pl1)##
            else:
                score = max(Mmin(board, score, pl1, pl2), score)
            pl1.pop()
    return score


def Mmin(board, score, pl1, pl2 ):
    score = 0
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            #print(square)##
            pl2.append(square)
            if checkWin(pl2) == 'win':
                score = -1
                #print(pl2)##
            else:
                score = min(Mmax(board, score, pl1, pl2), score)
            pl2.pop()
    return score

def comPlay(board, pl1, pl2):
    score = 0
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            #print(square)##
            pl1.append(square)
            score =  Mmin(board, score, pl1, pl2)
            pl1.pop()
            if score != -1:
                print(score)
                return square

out = comPlay(board, pl1, pl2)
print(out)