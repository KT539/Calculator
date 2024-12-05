import unittest
from src.MathLib import MathLib

class TestMathLib(unittest.TestCase):

    def setUp(self):
        self.math_lib = MathLib()

    def test_addition(self):
        result = self.math_lib.calculate(3, '+', 2)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.math_lib.calculate(5, '-', 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):

        result = self.math_lib.calculate(4, '*', 3)
        self.assertEqual(result, 12)

    def test_exponentiation(self):
        result = self.math_lib.calculate(2, '**', 3)
        self.assertEqual(result, 8)

    def test_division(self):
        result = self.math_lib.calculate(10, '/', 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        result = self.math_lib.calculate(10, '/', 0)
        self.assertIsNone(result)

    def test_invalid_operator(self):
        result = self.math_lib.calculate(10, '#', 2)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()