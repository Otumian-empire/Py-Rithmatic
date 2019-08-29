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

	def test_add_no_args(self):
		self.assertEqual(self.app.add(), 0)
		

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
	
	
	def test_multi_int_type(self):
		self.assertTrue(type(self.app.multi([2, 1])) == int)

	def test_multi_float_type(self):
		self.assertTrue(type(self.app.multi([2.1, 1.2])) == float)

	def test_multi_int_rval(self):
		self.assertEqual(self.app.multi([2, 1]), 2)

	def test_multi_float_rval(self):
		self.assertEqual(self.app.multi([2.4, 1.2]), 2.88) 

	def test_multi_empty_args(self):
		self.assertEqual(self.app.multi([]), 0)

	def test_multi_no_args(self):
		self.assertEqual(self.app.multi(), 0)


	def test_div_float_type(self):
		self.assertTrue(type(self.app.div(5, 2)), float)

	def test_div_float_rval(self):
		self.assertEqual(self.app.div(5, 2), 2.5)

	def test_div_epmty_args(self):
		self.assertEqual(self.app.div(), 0)

	def test_div_zero_division(self):
		self.assertEqual(self.app.div(1, 0), 0)


	def test_divfloor_int_type(self):
		self.assertTrue(type(self.app.div_floor(5, 2)), int)

	def test_divfloor_float_rval(self):
		self.assertEqual(self.app.div_floor(5, 2), 2)

	def test_divfloor_epmty_args(self):
		self.assertEqual(self.app.div_floor(), 0)

	def test_divfloor_zero_division(self):
		self.assertEqual(self.app.div(1, 0), 0)

	
	def test_mod_int_type(self):
		self.assertTrue(type(self.app.mod(23, 4)), int)

	def test_mod_int_rval(self):
		self.assertEqual(self.app.mod(23, 4), 3)

	def test_mod_empty_args(self):
		self.assertEqual(self.app.mod(), 0)

	def test_mod_zero_division(self):
		self.assertEqual(self.app.mod(23, 0), 0)


	def test_divmod_int_type(self):
		self.assertTrue(type(self.app.div_mod(23, 4)), tuple)

	def test_divmod_int_rval(self):
		self.assertEqual(self.app.div_mod(23, 4), (5, 3))

	def test_divmod_empty_args(self):
		self.assertEqual(self.app.div_mod(), (0, 0))

	def test_divmod_zero_division(self):
		self.assertEqual(self.app.div_mod(23, 0), (0, 0))

unittest.main()
