# Greets
print('This program will determine the amount of time it would take to download all the words ever spoken for a given connection speed.\n')

speed = float(input('What is your connection speed (Mbps)? '))

"""
Assume the download speed is 50Mbps.
The all words ever spoken was approximately 5 exabytes of data from the book. Which is 10^18 (1,000,000,000,000,000,000) * 5 byte
"""

# Calculations

words = (10 ** 18) * 5 # Converting 5 exbytes to byte
year_second = 31536000 # Year to seconds
seconds = words / ((speed * 0.125) * (10 ** 6))
years = seconds / year_second

# Printing result
print('The total time to download all words ever spoken for your connection speed is approximately', format(years, ',.0f'), 'years')