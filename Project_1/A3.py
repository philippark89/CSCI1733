# Flags
ask = True

# Looping until user input is 'No'
while ask:

	# Main Menu
	print()
	print('Enter desired conversion')
	print('------------------------')
	print('1 - pounds / grams')
	print('2 - inches / centimeters')
	print('3 - miles / kilometers')
	print()

	enter = int(input('Enter: '))

	# First option
	if enter == 1:
		ch = input('(a) pounds to grams, or (b) grams to pounds: ')
		if ch == 'a':
			enter = float(input('\nEnter number of pounds: '))
			pounds = 453.59 * enter

			print(enter, 'pounds is equal to', pounds, 'grams')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

		elif ch == 'b':
			enter = float(input('\nEnter number of grams: '))
			grams = 0.0022 * enter

			print(enter, 'grams is qequal to', grams, 'pounds')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

	# Second option
	elif enter == 2:
		ch = input('(a) inches to cm, or (b) cm to inches: ')
		if ch == 'a':
			enter = float(input('\nEnter number of inches: '))
			centimeters = 2.54 * enter

			print(enter, 'inches in equal to', centimeters, 'centimeters')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

		elif ch == 'b':
			enter = float(input('\nEnter number of centimeters: '))
			inches = 0.39 * enter

			print(enter, 'centimeters is equal to', inches, 'inches')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

	# Third option
	elif enter == 3:
		ch = input('(a) miles to kilometers, or (b) km to miles: ')
		if ch == 'a':
			enter = float(input('\nEnter number of miles: '))
			kilometers = 1.61 * enter

			print(enter, 'miles is equal to', kilometers, 'kilometers')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

		elif ch == 'b':
			enter = float(input('\nEnter number of kilometers: '))
			miles = 0.62 * enter

			print(enter, 'kilometers is equal to', miles, 'miles')
			print()

			yorn = input('Do you wish to do another conversion (y/n): ')
			if yorn == 'n':
				ask = False

	else:
		print('Chose number between 1 - 3')

print('Goodbye ...')