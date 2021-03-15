
dict = { 'a2' : [ 'X', { 'c1' : ['X', 'win'] } ], 'b1' : ['O', 'lose'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'win'] }]}] }

#search for 'win' in nested dictionary
deapth = 0
currDeapth = []
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
		if dict == 'win':
			currDeapth.append(deapth)
		deapth += -1
	return currDeapth
	
print(searchDeapth(dict, deapth, currDeapth))
			
		
	


