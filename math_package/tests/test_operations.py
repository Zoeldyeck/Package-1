import unittest
from math_package import add, subtract, multiply, divide
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2),3)

    def test_subtract(self):
        self.assertEqual(subtract(2,1),1)    

    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
         divide(10,0)


if __name__=='__main__':
    unittest.main()         
