
dict = { 'a2' : [ 'X', { 'c1' : ['X', 'L'], 'a1' : ['O', 'W'] } ],'a3' : [ 'O' ], 'b1' : ['O', 'L'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'W'] }]}] }

#search for 'win' in nested dictionary
deapth = 0
currDeapth = []
temp = []#
def searchDeapth(dict, deapth, currDeapth):
	if type(dict) == type({ 'key' : 'value' }):
		deapth += 1
		for key in dict:
			searchDeapth(dict[key], deapth, currDeapth)
	elif type(dict) == type(['value']):
		deapth += 1
		for item in dict:
			searchDeapth(item, deapth, currDeapth)
	elif type(dict) == type('string'):
		if dict == 'W' or dict == 'L':
			currDeapth.append(deapth//2)
		deapth += -1
		temp.append(dict)#
	return currDeapth, temp#
	
outdep, out = searchDeapth(dict, deapth, currDeapth)
test = ''.join(out)
print(test)
plays = []
for i in outdep:
	win = test.find('W')
	lose = test.find('L')
	if win == -1 and lose == -1:
		break
	elif win == -1:
		win = lose +1
	elif lose == -1:
		lose = win +1
	if win > lose:
		this = lose
	elif lose > win:
		this = win
	play = test[ this-i : this +1 ]
	#print('play', play)
	plays.append(play)
	test = test[ this+1 : ]
print(plays)
print(outdep)
			
		
	


