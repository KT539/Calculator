import unittest

from src.MathRequest import MathRequest

class TestMathRequest(unittest.TestCase):

    def setUp(self):
        self.ope1 = 3
        self.ope = "add"
        self.ope2 = 5
        self.mathRequest = MathRequest(self.ope1, self.ope, self.ope2)

    def test_get_ope1(self):
        self.assertEqual(self.mathRequest.get_ope1(), self.ope1)

    def test_get_ope(self):
        self.assertEqual(self.mathRequest.get_ope(), self.ope)

    def test_get_ope2(self):
        self.assertEqual(self.mathRequest.get_ope2(), self.ope2)

if __name__ == '__main__':
    unittest.main()