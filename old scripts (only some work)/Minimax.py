'''
FINALLY IT WORKS FOR both players


'''

from player_only_TicTacToe import *


def minimax(board, turn, score, pl1, pl2):
    if turn == '1' : pl, turn, score = pl1, '2', -1 #setting up pl and score for the min/max player
    elif turn == '2' : pl, turn, score = pl2, '1', 1 #FLIPPING TURN for next player
    best = ''
    for square in board:
        if isValid(board, square, pl1, pl2) == 'valid':
            pl.append(square)
            win = checkWin(pl, (len(pl1)+len(pl2)))
            if win == 'draw':
                score = 0
                best = square
            elif win == 'win':
                if turn == '2': score = 1
                elif turn == '1': score = -1 # TURN IS FLIPPED HERE
                best = square
            else:
                newscore, _ = minimax(board, turn, score, pl1, pl2)
                if (newscore > score and turn == '2') or (newscore < score and turn == '1'):
                    score = newscore # TURN IS FLIPPED IN ABOVE LINE
                    best = square
            pl.pop()
    return score, best




def startGame(): # start game
    #getting board ready
	board = genBoard()
	printBoard(board)
	
	
	while True: # ask is pvp or pvc
		opponent = input('PVP(P) or PVC(C) ?:').upper()
		if opponent == 'P' or opponent == 'C': break
		else: print('type either p or c (case dosent matter)')
	
	
	playas = '' # ask what player human wants to play as
	while opponent == 'C':
		playas = input('play as player 1 or 2 ?: ')
		if playas == '1' or playas == '2': break
		else: print('type either 1 or 2')
	
	
	# switch turns
	pl1, pl2 = [], [] 
	for i in range(9):
		if i%2 == 0: # player 1
			turn = '1X'
		else: # player 2
			turn = '2O'
	
	
		# choose what player plays next (ai or human)
		if turn[0] == playas or opponent == 'P': # human
			valid = 'no' # reset var for next turn
			while valid == 'no': # check if play is valid
				play = input(f'player {turn[0]} ({turn[1]}) input coords: ')
				valid = isValid(board, play, pl1, pl2)
				if valid == 'no':
					print('\nPLAY NOT VALID. TRY AGAIN\n')
		else: # computer's turn
			score = 0
			_, play =  minimax(board, turn[0], score, pl1, pl2)
		
		# print board
		board[play] = f'{turn[1]}'
		printBoard(board)
		
		# set result if game ends
		if i%2 == 0: # player 1
			pl1.append(play)
			result = checkWin(pl1, (len(pl1)+len(pl2)))
		else: # player 2
			pl2.append(play)
			result = checkWin(pl2)
			
		if result: # display appropriate message when game ends
			if opponent == 'P':
				if result == 'win': print(f'PLAYER {turn[0]} ({turn[1]}) HAS WON!!')
				elif result == 'draw': print('its a draw')
			elif opponent == 'C':
				if result == 'win': print('you inefficient humans can\'t win against us')
				elif result == 'draw': print('a draw is the best you can achieve against us')
			break



startGame()
