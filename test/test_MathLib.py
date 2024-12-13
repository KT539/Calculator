import unittest
from src.MathLib import MathLib
from src.MathRequest import MathRequest

class TestMathLib(unittest.TestCase):

    def setUp(self):
        self.math_lib = MathLib()

    def test_execute_add_get_result(self):
        #given
        math_request = MathRequest(3, "add", 2)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 5)

    def test_execute_sub_get_result(self):
        #given
        math_request = MathRequest(5, "sub", 3)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 2)

    def test_execute_mul_get_result(self):
        #given
        math_request = MathRequest(4, "mul", 3)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 12)

    def test_execute_pow_get_result(self):
        #given
        math_request = MathRequest(2, "pow", 3)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 8)

    def test_execute_div_get_result(self):
        #given
        math_request = MathRequest(10, "div", 2)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 5)

    def test_execute_root_get_result(self):
        #given
        math_request = MathRequest(4, "root", 2)
        #when
        self.math_lib.execute(math_request)
        #then
        self.assertEqual(math_request.get_res(), 2)


if __name__ == '__main__':
    unittest.main()