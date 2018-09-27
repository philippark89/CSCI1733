# Using datetime to get current times
import datetime

# Greets
print('This program will list all leap years from the current year to a specified ending year')
print()

# Get current year
current_year = datetime.date.today().year

# Set the year from user input
input_year = int(input('Enter last year of range: '))


print('The following are leap years from', current_year, 'to', input_year, '\n')

while current_year <= input_year:
	if current_year % 4 == 0 and (not (current_year % 100 == 0) or (current_year % 400 == 0)):
		print(current_year)

	current_year = current_year + 1
