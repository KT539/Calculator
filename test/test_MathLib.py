import unittest
from src.MathLib import MathLib
from src.MathRequest import MathRequest

class TestMathLib(unittest.TestCase):

    def setUp(self):
        self.math_lib = MathLib()

    def test_addition(self):
        math_request = MathRequest(3, '+', 2)
        self.math_lib.calculate(math_request)
        self.assertEqual(math_request.get_res(), 5)

    def test_subtraction(self):
        math_request = MathRequest(5, '-', 3)
        self.math_lib.calculate(math_request)
        self.assertEqual(math_request.get_res(), 2)

    def test_multiplication(self):
        math_request = MathRequest(4, '*', 3)
        self.math_lib.calculate(math_request)
        self.assertEqual(math_request.get_res(), 12)

    def test_exponentiation(self):
        math_request = MathRequest(2, '**', 3)
        self.math_lib.calculate(math_request)
        self.assertEqual(math_request.get_res(), 8)

    def test_division(self):
        math_request = MathRequest(10, '/', 2)
        self.math_lib.calculate(math_request)
        self.assertEqual(math_request.get_res(), 5)


if __name__ == '__main__':
    unittest.main()