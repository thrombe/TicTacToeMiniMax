
from terminal_tic_tac_toe import *


#pl is a list of player moves
#board = genBoard()
board = { 'a1' : 'X', 'a2' : 'O', 'a3' : '.', 'b1' : 'O', 'b2' : '.', 'b2' : '.', 'b3' : 'X', 'c1' : '.', 'c2' : 'X', 'c3' : 'O' }
#pl1 , pl2 = [], []
pl1 = ['a1', 'b3', 'c2'] # CHANGING LISTS IN FUNC FUCKS IT UP
pl2 = ['a2', 'b1', 'c3']
out = {}
def playComp(board, pl1, pl2, out, turn = 'X', deep = 0):
	deep += 1
	#print(deep)
	for square in board.keys():
		p1 = pl1.copy()
		p2 = pl2.copy()
		#print(deep)
		print(square)
		movevalid = isValid(board, square, p1, p2)
		print(movevalid)
		if movevalid == 'valid':
			#print(square)
			if turn == 'X':
				p1.append(square)
				pl = p1
			if turn == 'O':
				p2.append(square)
				pl = p2
			print(p1, p2)
			board[square] = turn
			#print(pl1)
			if turn == 'X':
				turnnew = 'O'
			elif turn == 'O':
				turnnew = 'X'
			win = checkWin(pl)
			if win:
				if turn == 'X': out[square] = 'W'
				elif turn == 'O': out[square] = 'L'
				win = ''
				continue
			#out[square] = deep #
			move = playComp(board, p1, p2, out, turnnew, deep)
			out[square] = move
			#pl.pop()
		
		
	printBoard(board)
		#print(pl)
		#print(out)
	#print(out)
	print('return')
	#pl1.pop()
	#pl2.pop()
	return out



retu = playComp(board, pl1, pl2, out)
#print(retu['a3']['a3']['a3']['a3']['a3']['a3'])
print(retu)
#print(pl1)