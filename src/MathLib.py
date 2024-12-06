from src.MathRequest import MathRequest

class MathLib:
    def __init__(self):
        pass

    def calculate(self, math_request):
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()
        ope = math_request.get_ope()
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

        math_request.set_res(result)
        return math_request

