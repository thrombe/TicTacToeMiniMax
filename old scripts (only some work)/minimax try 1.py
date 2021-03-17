
'''
currently ai dosent lose as player 1, but dosent win either.
it draws every game.
as player 2, it dosent do very good job.
the first play is always is at c3, cuz loop ends at c3.



'''

from terminal_tic_tac_toe import *


def Mmax(board, score, pl1, pl2, ):
    score = -1
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
    score = 1
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            #print(square)##
            pl2.append(square)
            if checkWin(pl2) == 'win':
                score = -1
                #print(score)##
                #print(pl2)##
            else:
                score = min(Mmax(board, score, pl1, pl2), score)
            pl2.pop()
    return score

# plays 1 move and passes to minimax for deciding if its a good move
def comPlay(board, pl1, pl2):
    score = 0
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            #print(square)##
            pl1.append(square)
            if checkWin(pl1) == 'win':
            	pl1.pop()
            	return square
            score =  Mmin(board, score, pl1, pl2)
            pl1.pop()
            print(score)##
            print(square)##
            if score != -1:
                bestNonWin = square
                #print(score)##
                #print(square)##
                pass
    return bestNonWin




def startPvc():
    #getting board ready
	board = genBoard()
	printBoard(board)
	
	#start game
	pl1, pl2 = [], [] 
	for i in range(9):
		if i%2 == 0: # player 1
			turn = '1X'
		else: # player 2
			turn = '2O'
			
		# CHANGE 2 TO 1 AND 1 TO 2 HERE FOR PLAYER CHANGE
		if turn[0] == '1':
			valid = 'no' # reset var for next turn
			while valid == 'no': # check if play is valid
				play = input(f'player {turn[0]} ({turn[1]}) input coords: ')
				valid = isValid(board, play, pl1, pl2)
				if valid == 'no':
					print('\nPLAY NOT VALID. TRY AGAIN\n')
		elif turn[0] == '2':
			play = comPlay(board, pl1, pl2)
		
		# print board
		board[play] = f'{turn[1]}'
		printBoard(board)
		
		#check if win
		if i%2 == 0: # player 1
			pl1.append(play)
			result = checkWin(pl1)
		else: # player 2
			pl2.append(play)
			result = checkWin(pl2)
			
		if result:
			print(f'PLAYER {turn[0]} ({turn[1]}) HAS WON!!')
			break



startPvc()




if __name__ == '__maain__':
    board = genBoard()
    pl1, pl2 = ['a1', 'b2'], ['b1', 'c1']
    out = comPlay(board, pl1, pl2)
    print(out)
