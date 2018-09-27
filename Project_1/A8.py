# List of alphabets and morse codes
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.--.', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
words = []
codes = []

flag = True
empty = ''
final = ''

# Greets
print('This program will convert between English and Morse code.')
sel = input('(E)nglish to Morse code, or (M)orse code to English? ')

# Main menu begins
if sel == 'E':
	print()
	print('Enter English message, one sentence per line.')
	print('End each sentence with a period (hit return when done)')
	
	# Enter sentences
	while flag:
		enter = input()
		words.append(enter.lower())

		if enter == empty:
			flag = False
	
	for i in range(len(words)):	 		# amount of sentences
		for j in range(len(words[i])):	# amount of words in list
			for x in range(len(alpha)):	# length of alpha which 26
				if words[i][j] == alpha[x]:
					print(morse[x])

			if words[i][j] == ' ':
				print()
			elif words[i][j] == '.':
				print()	

elif sel == 'M':
	print()
	print('Enter morse-coded letters one per line.')
	print('Include one blank line between words, and two blank lines between sentences')
	done = input("(enter 'q' when done)\n")

	# Looping until user input 'q'
	while done != 'q':
		codes.append(done)
		done = input()

	for i in range(len(codes)):		# amount of list
		for j in range(len(morse)):	# amount of morse which is 26
			if codes[i] == morse[j]:
				final += alpha[j]

		if codes[i] == empty and codes[i+1] == empty:
			final += '.\n'

		elif codes[i] == empty and codes[i-1] != empty:
			final += ' '

print()
print(final.upper(), end='.\n')