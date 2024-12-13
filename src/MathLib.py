from src.MathRequest import MathRequest

class MathLib:
    def __init__(self):
        pass

    def calculate(self, math_request):
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()
        ope = math_request.get_ope()

        match ope:
            case "add":
                math_request.set_res(ope1 + ope2)
            case "sub":
                math_request.set_res(ope1 - ope2)
            case "mul":
                math_request.set_res(ope1 * ope2)
            case "power":
                math_request.set_res(ope1 ** ope2)
            case "root":
                if ope1 < 0 and ope2 % 2 == 0:
                    print("Error: Cannot calculate even root of a negative number.")
                    return None
                if ope2 == 0:
                    print("Error: Division by zero is undefined in root calculation.")
                    return None
                math_request.set_res(ope1 ** (1 / ope2))
            case "div":
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return None
                math_request.set_res(ope1 / ope2)
            case _:
                print("Invalid operator.")
                return None

        return math_request.get_res()

