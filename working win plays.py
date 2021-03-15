
#dict = { 'a2' : [ 'X', { 'c1' : ['X', 'win'] } ], 'b1' : ['O', 'lose'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'win'] }]}] }
#dict = { 'a2' : [ 'X', { 'c1' : ['X', 'L'], 'b3' : [ 'O', 'D' ], 'a1' : ['O', 'W'] } ],'a3' : [ 'O', 'D' ], 'b1' : ['O', 'L'], 'c1' : ['O', {'c3' : ['X', { 'b2' : ['O', 'W'] }]}] }
dict = { 
				'a2' : [ 'X', { 
									'c1' : ['X', 'L'], 
									'b3' : [ 'O', 'D' ],
									 'a1' : ['O', 'W'] 
								  } 
						  ],
				'a3' : [ 'O', 'D' ],
				 'b1' : ['O', {
				 				   'c3' : ['X', 'D'],
				 				   'c2' : ['O', 'W']
				 				  }
				 		  ],
				 'c1' : ['O', {
				 				  'c3' : ['X', { 'b2' : ['O', 'W'] }]
				 				 }
				 		  ] 
			}



#search for wins in nested dictionary
def searchWins(dict):
	deapth = 0
	currDeapth = []
	playlist = []
	play =''
	def searchDeapth(dict, deapth, currDeapth, play, playlist):
		
		
		
		if type(dict) == type({ 'key' : 'value' }):
			deapth += 1
			for key in dict:
				currDeapth.append(key)
				play += key
				ret = searchDeapth(dict[key], deapth, currDeapth, play, playlist)
				play = play[ : len(play)-2]
				
		
		
		elif type(dict) == type(['value']):
			deapth += 1
			for item in dict:
				searchDeapth(item, deapth, currDeapth, play, playlist)
		
		
		
		elif type(dict) == type('string'):
			if dict == 'W':
				currDeapth.append('W')
				play += 'W'
				playlist.append(play)
			elif dict == 'L':
				currDeapth.append('L')
				play += 'L'
				playlist.append(play)
			elif dict == 'D':
				currDeapth.append('D')
				play += 'D'
				playlist.append(play)
			deapth += -1
			
		
		
		
		return playlist
		
	out = searchDeapth(dict, deapth, currDeapth, play, playlist)
	opt = []
	for i in range(len(out)):
		#print(i)
		if 'L' in out[i]:
			dele = out[i][ : len(out[i])-3]
			#print(dele)
		if not dele:
			dele = 'shhwueii'
		if dele not in out[i] and 'W' in out[i]:
			#print(out[i])
			opt.append(out[i])
	return opt


if __name__ == '__main__':
	print(searchWins(dict))

			
		
	


