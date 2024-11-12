import unittest
from All_Functions_1 import is_prime
from All_Functions_1 import is_even
class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertTrue(is_prime(2))
    def test_five(self):
        self.assertTrue(is_prime(5))
    def test_nine(self):
        self.assertFalse(is_prime(9))
    def test_eleven(self):
        self.assertTrue(is_prime(11))
#    def test_seven(self):
#        self.assertTrue(is_even(10))
    def test_seven(self):
        self.assertFalse(is_even(9))
if __name__=='__main__':
    unittest.main()