# Author: Otumian [-Empire]
# Github account: https://github.com/Otumian-empire
# Email: popecan1000@gmail.com
# Library name: Arithmatic
# Repository url" https://github.com/Otumian-empire/pyrithmatic.git
# Description:
# 	an abstraction layer on the arithmatic operators
# 	for basic arithmatic operations such as:
# 	addition, subtraction, multiplication, division, floor division,
# 	modulo, power

class Arithmatic:
	""" Arithmatic: an abstraction layer on the arithmatic operators """

	def __init__(self):
		print("imported Arithmatic: successful")

	def add(self, iterable_arg = []):
		"""
		function: add
		argument: iterable: [int, float]
		use: add([1,2,3,4,5])
		description: returns the sum of elements in the iterable_arg, this is similar to sum
		"""
		try:
			val_sum = 0
			if iterable_arg:
				for i in iterable_arg:
					val_sum += i
				
				return val_sum
			return val_sum
		except Exception as e:
			print(e)

	def subtr(self, first_number = 0, second_number = 0):
		"""
		function: subtr
		arguments: first_number:[int, float], second_number:[int, float]
		use: subtr(1, 2.1)
		description: returns the difference between first_number and second_number
		"""
		try:
			return first_number - second_number
		except Exception as e:
			print(e)

	def multi(self, iterable_arg = []):
		"""
		function: multi
		argument: iterable: [int, float]
		use: multi([1,2,3,4,5])
		description: returns the product of elements in the iterable.
		"""
		try:
			val_sum = 1
			if iterable_arg:
				for i in iterable_arg:
					val_sum *= i
				
				return val_sum
			return 0
		except Exception as e:
			print(e)

	def div(self, first_number = 0, second_number = 1):
		"""
		function: div
		arguments: first_number:[int, float], second_number:[int, float]
		use: div(1, 2.1)
		description: returns a float when second_number divides first_number
		"""
		try:
			if second_number:
				return first_number / second_number
			else:
				print(f"second_number given {second_number}, use an int/float gt {0.0!r}")
				return 0
		except Exception as e:
			print(e)

	def div_floor(self, first_number = 0, second_number = 1):
		"""
		function: div_floor
		arguments: first_number:[int, float], second_number:[int, float]
		use: div_floor(1, 2.1)
		description: returns the quotient (int) when second_number divides first_number
		pow
		"""
		try:
			if second_number:
				return first_number // second_number
			else:
				print(f"second_number given {second_number}, use an int/float gt {0.0!r}")
				return 0
		except Exception as e:
			print(e)

	def mod(self, first_number = 0, second_number = 1):
		"""
		function: mod
		arguments: first_number:[int, float], second_number:[int, float]
		use: mod(1, 2.1)
		description: returns a remainder when second_number divides first_number
		"""
		try:
			if second_number:
				return first_number % second_number
			else:
				print(f"second_number given {second_number}, use an int/float gt {0.0!r}")
				return 0
		except Exception as e:
			print(e)

	def div_mod(self, first_number = 0, second_number = 1):
		"""
		function: div_mod
		arguments: first_number:[int, float], second_number:[int, float]
		use: div_mod(1, 2.1)
		description: returns a tuple, of the quotient and  remainder when second_number divides first_number
		"""
		try:
			if second_number:
				return (first_number // second_number) , (first_number % second_number)
			else:
				print(f"second_number given {second_number}, use an int/float gt {0.0!r}")
				return (0, 0)
		except Exception as e:
			print(e)

	def pow(self, first_number = 1, second_number = 0):
		"""
		function: pow
		arguments: first_number:[int, float], second_number:[int, float]
		use: pow(1, 2.1)
		description: returns first_number raised to the exponent, second_number
		"""
		try:
			if first_number:
				return first_number ** second_number
			else:
				print(f"first_number given {first_number}, use an int/float gt {0.0!r}")
				return 0
		except Exception as e:
			print(e)
