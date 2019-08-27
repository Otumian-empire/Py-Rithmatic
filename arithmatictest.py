# this is a test file.
# import Arithmatic module

from arithmatic import Arithmatic
import unittest


class ArithmaticTest(unittest.TestCase):
	app = Arithmatic()

	def test_add_int_type(self):
		self.assertTrue(type(self.app.add([1, 2]) in [int, float]))

	def test_add_float_type(self):
			self.assertTrue(type(self.app.add([1.2, 2.1]) in [int, float]))

	def test_add_int_rval(self):
		self.assertEqual(self.app.add([1, 2]), 3)

	def test_add_float_rval(self):
		self.assertEqual(self.app.add([1.2, 2.1]), 3.3)

	def test_add_empty_ite(self):
		self.assertEqual(self.app.add([]), 0)

unittest.main()
