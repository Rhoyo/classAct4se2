import pal
import unittest

def test_answer():
	assert(pal.pal("follow")==1)

strin='92329'

class palT(unittest.TestCase):

	def test_type(self):
		self.assertIsInstance(strin, str)
	
	def test_res(self):
		res=pal.pal(strin)
		self.assertIsInstance(res,int)
