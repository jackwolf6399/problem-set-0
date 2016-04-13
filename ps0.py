# 0
def is_even(number):
	''' Tells if number is even or not '''
	even = number % 2
	return even == 0
	
# 1
def numb_digits(number):
	''' Returns the number of digits in a number '''
	number = str(number)
	digits = len(number)
	return digits

# 2
def sum_digits(number):
	''' Sums up all the digits in a number '''
	sum = 0
	for digit in str(number):
		sum += int(digit)
	return sum
	
# 3
def lesser_numbers(number):
	''' Sums up all the numbers that are lesser than given number '''
	sum = 0
	while number != 0:
		sum = sum + number
		number = number - 1
	return sum
	
# 4
def factorial(number):
	''' Takes the factorial of a number '''
	product = 1
	if number == 0:
		return product
	else:
		while number != 1:
			product = product * number
			number = number - 1
	return product
		
# 5
def factor(number, factor):
	''' Sees if second number is factor of first number '''
	yes = factor % number
	return yes == 0
		
# 6
def prime(number):
	''' Sees if a number is prime '''
	divisors = number - 1
	while divisors > 1:
		remainder = number % divisors
		divisors = divisors - 1
		if remainder == 0:
			return "False"
	else:
		return "True"
	
# 7
def perfect(number):
	''' Sees if a number is perfect '''
	sum = 0
	factor = number - 1
	while factor > 0:
		remainder = number % factor
		if remainder == 0:
			sum += factor
		factor = factor - 1	
	if sum == number:
		return "True"
	else:
		return "False"
		
	

# 8 
def sum_divisor(number):
	''' Sees if the sum of the digits divides evenly into the number '''
	sum = sum_digits(number)
	if number % sum == 0:
		return "True"
	else:
		return "False"


