# Author: Otumian (Empire)
# Github account: https://github.com/Otumian-empire
# Email: popecan1000@gmail.com
# Library name: Arithmatic
# Arithmatic: an abstraction layer on the math lib
# 	Description:
#		for basic arithmatic operations such as:
# 	addition, subtraction, multiplication, division, floor division,
# 	modulo, power
# 	aside from that, it is the math std-lib
# Resource:
#		https://docs.python.org/3.6/library/math.html?highlight=math#module-math
# 	https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html


class Arithmatic:
	""" Arithmatic: an abstraction layer on the arithmatic operators """

	def __init__(self):
		print("imported Arithmatic: successful")

	def add(self, iterable_arg = []):
		"""
		function: add
		argument: iterable: [int, float]
		use: add([1,2,3,4,5])
		description: returns the sum of the iterable, this is similar to sum
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
			return val_sum
		except Exception as e:
			print(e)

	def div(self, first_number, second_number):
		"""
		"""
		pass

	def div_floor(self, first_number, second_number):
		"""
		"""
		pass

	def mod(self, first_number, second_number):
		"""
		"""
		pass

	def div_mod(self, first_number, second_number):
		"""
		"""
		pass

	def pow(self, first_number, second_number):
		"""
		"""
		pass
