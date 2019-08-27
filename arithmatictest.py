# this is a test file.
# import Arithmatic module

from arithmatic import Arithmatic
import unittest


class ArithmaticTest(unittest.TestCase):
	app = Arithmatic()

	def test_add_int_type(self):
		self.assertTrue(type(self.app.add([1, 2]) == int))

	def test_add_float_type(self):
			self.assertTrue(type(self.app.add([1.2, 2.1]) == float))


	def test_add_int_rval(self):
		self.assertEqual(self.app.add([1, 2]), 3)

	def test_add_float_rval(self):
		self.assertEqual(self.app.add([1.2, 2.1]), 3.3)


	def test_add_empty_ite(self):
		self.assertEqual(self.app.add([]), 0)


	def test_subtr_int_type(self):
		self.assertTrue(type(self.app.subtr(2, 1) == int))

	def test_subtr_float_type(self):
			self.assertTrue(type(self.app.subtr(2.1, 1.2) == float))

	
	def test_subtr_int_rval(self):
		self.assertEqual(self.app.subtr(2, 1), 1)

	def test_subtr_float_rval(self):
		self.assertEqual(self.app.subtr(2.4, 1.2), 1.2) 


	def test_subtr_empty_args(self):
		self.assertEqual(self.app.subtr(), 0)
unittest.main()
