"""
Sample script to test ad-hoc scanning by table drive.
This accepts time in 24hour format (xx:xx, x:xx, x.xx, xx.xx) 
"""

def getchar(words,pos):
	""" returns groupChars at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	

	if words[pos] >= '0' and words[pos] <= '1':
		return 'time_0'

	elif words[pos] == '2':
		return 'time_1'

	elif words[pos] >= '3' and words[pos] <= '9':
		return 'time_2'
	
	elif words[pos] >= '0' and words[pos] <= '3':
		return 'time_3'
	
	elif words[pos] >= '0' and words[pos] <= '5':
		return 'time_4'

	elif words[pos] >= '0' and words[pos] <= '9':
		return 'time_5'

	elif words[pos] == ':' or words[pos] == '.':
		return 'time_sep'

	else:
		return 'OTHER'



	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char

			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary
td = { 
		'q0' : {'time_0' : 'q1', 'time_1' : 'q2', 'time_2' : 'q3', 'OTHER':'q9'},
		'q1' : {'time_sep' : 'q6','time_5': 'q4', 'OTHER':'q9'},
		'q2' : {'time_sep' : 'q6', 'time_3': 'q5', 'OTHER':'q9' },
		'q3' : {'time_sep' : 'q6','OTHER':'q9'},
		'q4' : {'time_sep' : 'q6', 'OTHER':'q9'},
		'q5' : {'time_sep' : 'q6', 'OTHER':'q9'},
		'q6' : {'time_4': 'q7', 'OTHER':'q9'},
	        'q7' : {'time_5': 'q8', 'OTHER':'q9'}
     } 


# the dictionary of accepting states and their
# corresponding token
ad = {'q8' : 'TIME_TOKEN',
      'q9' : 'WRONG INPUT'
}




# get a string from input
text = input('give some input>')



# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('ERROR_TOKEN: unrecognized input at pos',position+1,'of',text)
		break
	
	print(token,text[:position])
	
	# remaining text for next scan

	text = text[position: ]
