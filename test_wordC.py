import wordC
import unittest


def test_answer():
	assert wordC.wordC(" cool ")==1


sent="no_1 2"

class palT(unittest.TestCase):

	def test_type(self):
		self.assertIsInstance(sent, str)
		res= wordC.wordC(sent);

	def test_empty(self):
		self.assertTrue(sent)
		res= wordC.wordC(sent);



