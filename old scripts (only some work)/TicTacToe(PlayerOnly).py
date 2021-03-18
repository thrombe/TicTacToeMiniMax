

if __name__ == '__main__':
	print('''\
welcome to terminal tic-tac-toe or knots and krossess
or whatever you call this game

made by thrombe
''')
	input('press enter to start')

def genBoard():
	board  = {  }
	for i in range(9): #generating blank board with coords like a2 starting from top left
		x = ['a', 'b', 'c']
		y = ['1', '2', '3']
		board[ x[i%3] + y[i//3] ] = '.'
	return board

def printBoard(board):
	print(
			'\n' + '    a   b   c' + '\n\n'
			+ '1  ' + ' ' + board['a1'] + ' | ' + board['b1'] + ' | ' + board['c1'] 
			+ '\n   -----------\n' 
			+ '2  ' + ' ' + board['a2'] + ' | ' + board['b2'] + ' | ' + board['c2'] 
			+ '\n   -----------\n' 
			+ '3  ' + ' ' + board['a3'] + ' | ' + board['b3'] + ' | ' + board['c3'] 
			+ '\n'
			)


def checkWin(pl, total = 0): # checks if current player has won
	if len(pl) < 3: return 0 # if player has less moves than 3, dont bother checking
	pl = ''.join(pl)
	for i in 'abc123': # for vertical and horizontal
		if pl.count(i) == 3:
			return 'win'
	if 'b2' in pl: # for diagonals
		if 'a1' in pl and 'c3' in pl:
			return 'win'
		elif 'c1' in pl and 'a3' in pl:
			return 'win'
	if total == 9: return 'draw'

def isValid(board, play, pl1, pl2): # check if play valid or not
	if play in board: # check if play is valid coord
		if play not in pl1 and play not in pl2: # check if coord is already occupied
			return 'valid'
	return 'no'

def startGame():
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
		
		valid = 'no' # reset var for next turn
		while valid == 'no': # check if play is valid
			play = input(f'player {turn[0]} ({turn[1]}) input coords: ')
			valid = isValid(board, play, pl1, pl2)
			if valid == 'no':
				print('\nPLAY NOT VALID. TRY AGAIN\n')
		
		# print board
		board[play] = f'{turn[1]}'
		printBoard(board)
		
		#check if win
		if i%2 == 0: # player 1
			pl1.append(play)
			result = checkWin(pl1, (len(pl1)+len(pl2)))
		else: # player 2
			pl2.append(play)
			result = checkWin(pl2, (len(pl1)+len(pl2)))
			
		if result == 'win':
			print(f'PLAYER {turn[0]} ({turn[1]}) HAS WON!!')
			break
	
if __name__ == '__main__':
	startGame()
