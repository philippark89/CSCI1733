# Monthly Mortgage, range of interest rates from 3% to 18%
# P = (Ar(1 + r) ** n) / ((1 + r) ** n - 1)
# A is the loan amount 
# n is the number of total payments
# r is the annual interest rate divided by 12

# Init rates
rates = 3

# Greets
print('This program will display the monthly mortgage payments for a given loan amount and loan period for interest rates from 3% - 18%\n')

# Getting loan amount and years of loan
loan_amount = int(input('Enter loan amount: '))
years_loan = int(input('Enter number of years of loan: '))

print('Loan Amount: $', format(loan_amount, ',.2f'), 'Term:', years_loan, 'years')
print()

print('Interest Rate', format(' ', '<5'), 'Monthly Payment', format(' ', '<5'), 'Total Amount Paid')

# Looping interest rate 3% to 18%
while rates < 19:
	A = loan_amount
	n = years_loan * 12
	r = float((rates / 12) / 100)

	# Calculating mortgage payment
	P = float((A * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))
	
	monthly_pay = P
	# Calculating total amount paid
	total_amount = monthly_pay * years_loan * 12
	
	# Matching up the lines according to the example of assignment.
	if rates < 10:
		print('{:6d}'.format(rates), '%', '{:=22.2f}'.format(monthly_pay), '{:=23.2f}'.format(total_amount))
	else:
		print('{:7d}'.format(rates), '%', '{:=21.2f}'.format(monthly_pay), '{:=23.2f}'.format(total_amount))

	# Increasing rates
	rates += 1