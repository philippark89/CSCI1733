# First-Time home buyer tax credit of $8k
# bought a house that cost less than $800k
# had a combined income of under $225k
# had not owned a primary residence in the last three years.

# Greets
print('This program will determine if a person is eligible for a first-time home buyer federal tax credit')
print()

# Checking the purchase price
price = int(input('Enter purchase price: '))

# Checking the house price for eligibility
if price < 800000:
	income = int(input('Enter combined income: '))

	# Checking combined income
	if income < 225000:
		previously_owned = input('Have you previously owned a home (y/n)? ')

		# Checking if user owned home before.
		if previously_owned == 'n':
			print()
			print('CONGRATULATIONS!')
			print('Based on the information provided, you qualify for this tax credit')		
		elif previously_owned == 'y':
			years = int(input('How many years ago were you a home owner?: '))

			# Checking if user owned home last 3 years
			if years < 3:
				print()
				print('You do not qualify for this tax credit since you were a homeonwer within the last 3 years')
			else:
				print()
				print('CONGRATULATIONS!')
				print('Based on the information provided, you qualify for this tax credit')

		else:
			print('Type y or n')
	else:
		print()
		print('Your combined income exceeds the allowed maximum of $225,000')
		print('Therefore, you do not qualify for this tax credits')

# If purchase price is higher than 800k
else:
	print()
	print('The purchase price is limited to $800,000')
	print('Therefore, you do not qualify for this tax credit')