class MathLib:
    def calculate(self, ope1, ope, ope2):
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