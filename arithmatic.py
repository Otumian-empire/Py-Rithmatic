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
	""" Arithmatic: an abstraction layer on the math lib """

	def __init__(self):
		print("imported Arithmatic: successful")

	def add(self, iterable_arg):
		"""
		function: add
		argument: iterable
		use: add([1,2,3,4,5])
		description: returns the sum of the iterable, this is similar to sum
		"""
		try:
			val_sum = 0
			for i in iterable_arg:
				val_sum += i
		except Exception as e:
			return e
		finally:
			return val_sum
