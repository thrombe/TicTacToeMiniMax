
#dict = { 'a2' : [ 'X', { 'c1' : ['X', 'win'] } ], 'b1' : ['O', 'lose'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'win'] }]}] }
dict = { 'a2' : [ 'X', { 'c1' : ['X', 'L'], 'a1' : ['O', 'W'] } ],'a3' : [ 'O', 'D' ], 'b1' : ['O', 'L'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'W'] }]}] }

#search for 'win' in nested dictionary
deapth = 0
currDeapth = []
def searchDeapth(dict, deapth, currDeapth):
	ret = ''
	if type(dict) == type({ 'key' : 'value' }):
		deapth += 1
		for key in dict:
			currDeapth.append(key)
			searchDeapth(dict[key], deapth, currDeapth)
	elif type(dict) == type(['value']):
		deapth += 1
		for item in range(len(dict)):
			#currDeapth.append(item)
			if ret == 'break':
				print(ret)
				break
			ret = searchDeapth(dict[item], deapth, currDeapth)
	elif type(dict) == type('string'):
		if dict == 'W':
			#currDeapth.append('dep'+str(deapth))
			currDeapth.append('W')
		elif dict == 'L':
			del currDeapth[len(currDeapth)-1]
			#del currDeapth[len(currDeapth)-1]
			return 'break'
		elif dict == 'D':
			del currDeapth[len(currDeapth)-1]
		else:
			#del currDeapth[len(currDeapth)-1]
			pass
		deapth += -1
		
	return currDeapth
	
print(searchDeapth(dict, deapth, currDeapth))
			
		
	


