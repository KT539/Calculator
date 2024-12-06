class MockMathRequest:

    def __init__ (self, ope1, ope, ope2):
        self.ope1 = ope1
        self.ope = ope
        self.ope2 = ope2
        self.result = None

    def get_ope1(self):
        return self.ope1

    def get_ope(self):
        return self.ope

    def get_ope2(self):
        return self.ope2

    def get_res(self):
        return self.result

    def set_res(self, value):
        self.result =  value

    def to_string(self):
        raise NotImplementedError

class MathLib:
    @staticmethod
    def calculate(ope1, ope, ope2):
        match ope:
            case '+':
                return ope1 + ope2
            case '-':
                return ope1 - ope2
            case '*':
                return ope1 * ope2
            case '**':
                return ope1 ** ope2
            case '/':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return None
                return ope1 / ope2
            case _:
                print("Invalid operator.")
                return None

    @staticmethod
    def process_request(request):
        ope1 = request.get_ope1()
        ope = request.get_ope()
        ope2 = request.get_ope2()

        result = MathLib.calculate(ope1, ope, ope2)

        request.set_res(result)

        return request

