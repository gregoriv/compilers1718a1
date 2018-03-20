"""
Sample script to test ad-hoc scanning by table drive.
This accepts time in 24hour format (xx:xx, x:xx, x.xx, xx.xx) 
"""
def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	
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
			return 'ERROR_TOKEN',pos #returns ERROR_TOKEN and position when time is wrong
			
# the transition table, as a dictionary
# new transition table:
td = { 'q0':{ '0':'q1','1':'q1','2':'q2','3':'q3','4':'q3','5':'q3','6':'q3','7':'q3','8':'q3','9':'q3'},
       'q1':{ ':':'q6','.':'q6','0':'q4','1':'q4','2':'q4','3':'q4','4':'q4','5':'q4','6':'q4','7':'q4','8':'q4','9':'q4' },
       'q2':{ ':':'q6','.':'q6','0':'q5','1':'q5','2':'q5','3':'q5' },
       'q3':{ ':':'q6','.':'q6' },  
       'q4':{ ':':'q6','.':'q6' },
       'q5':{ ':':'q6','.':'q6' },
       'q6':{ '0':'q7','1':'q7','2':'q7','3':'q7','4':'q7','5':'q7' },
       'q7':{ '0':'q8','1':'q8','2':'q8','3':'q8','4':'q8','5':'q8','6':'q8','7':'q8','8':'q8','9':'q8' }	
     } 

# the dictionary of accepting states and their
# corresponding token
#new dictionary of accepting states:
ad = { 'q8':'TIME_TOKEN' } #returns TIME_TOKEN when time is correct

# get a string from input
text = input('give time>')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN': #if there is an ERROR_TOKEN print
		print('unrecognized input at pos',position+1,'of',text)
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
