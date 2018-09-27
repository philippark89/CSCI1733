# Greets
print('This program will display the day of the week that various holidays fall on for a given year, including a provided birth date.')
print()

# Lists
days = ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

month_31 = (1, 3, 5, 7, 8, 10, 12)
month_30 = (4, 6, 9, 11)

days_month = (28, 29, 30, 31)

holiday = [["New Year's Eve", months[11], 31], ["Valentine's Day", months[1], 14], ["St. Patricks's Day", months[2], 17], ["April Fool's Day", months[3], 1], ["Fourth of July", months[6], 4], ["Halloween", months[9], 31], ["Your Birthday", [0], [0]]]

enter_year = int(input('Enter year (yyyy) (-1 to quit): '))

# Enter -1 to exit
while enter_year != -1:
	print()
	# Leap year process
	if (enter_year % 4 == 0) and (not (enter_year % 100 == 0) or (enter_year % 400 == 0)):
		leap = True
	else:
		leap = False

	month = int(input("What month were you born? (1,...,12): "))
	while month < 1 or month > 12:
		print("Please enter between 1 and 12")
		month = int(input("What month were you born? (1,...,12): "))

	day = int(input("What day were you born? (1,...,12): "))

	# Checking if the select month is February or not
	if month == 2 and leap == False:
		while day < 1 or day > days_month[0]:
			print('Please enter between 1 and 28')
			day = int(input("What day were you born? (1,...,28): "))
	elif month == 2 and leap == True:
		while  day < 1 or day > days_month[1]:
			print('Please enter between 1 and 29')
			day = int(input("What day were you born? (1,...,29): "))
	elif month in month_30:
		while day < 1 or day > days_month[2]:
			print('Please enter between 1 and 30')
			day = int(input("What day were you born? (1,...,30): "))
	elif month in month_31:
		while day < 1 or day > days_month[3]:
			print('Please enter between 1 and 31')
			day = int(input("What day were you born? (1,...,31): "))

	#Storing user's birthday into the holiday list
	holiday[6][1] = month
	holiday[6][2] = day

	print()

	# Calender process
	for i in range(len(holiday)):
		century = enter_year // 100
		years = enter_year % 100
		x = years + (years // 4)

		if century == 18:
			x += 2
		elif century == 20:
			x += 6

		if holiday[i][1] == 1 and not leap:
			x += 1
		elif holiday[i][1] == 2:
			if leap:
				x += 3
			else:
				x += 4

		elif holiday[i][1] == 3 or holiday[i][1] == 11:
			x += 4
		elif holiday[i][1] == 5:
			x += 2
		elif holiday[i][1] == 6:
			x += 5
		elif holiday[i][1] == 8:
			x += 3
		elif holiday[i][1] == 9 or holiday[i][1] == 12:
			x += 6
		elif holiday[i][1] == 10:
			x += 1

		week = (x + holiday[i][2]) % 7

		print(holiday[i][0], 'falls on a', days[week])


	print('Labor Day falls on a Monday')
	print()

	enter_year = int(input('Enter year (yyyy) (-1 to quit): '))