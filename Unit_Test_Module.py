import unittest
from All_Functions_1 import is_prime
from All_Functions_1 import is_even
from All_Functions_1 import addNumbers
from All_Functions_1 import subtractNumbers
from All_Functions_1 import multiplyNumbers
from All_Functions_1 import divideNumbers
class TestPrime(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_prime(2))
    def test_2(self):
        self.assertFalse(is_prime(8))
    def test_3(self):
        self.assertTrue(is_even(10))
    def test_4(self):
        self.assertEqual(addNumbers(30,20), None)
    def test_5(self):
        self.assertEqual(subtractNumbers(50,20), None)
    def test_6(self):
        self.assertEqual(multiplyNumbers(80,20), None)
    def test_7(self):
        self.assertEqual(divideNumbers(40,20), None)
if __name__=='__main__':
    unittest.main()