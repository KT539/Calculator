from src.MathRequest import MathRequest
from src.MathLib import MathLib

class Main:
    def __init__(self):
        # Créer les instances des classes nécessaires
        self.math_request = MathRequest()
        self.math_lib = MathLib()

    def display_result(self, ope1, ope, ope2, res):
        print(str(ope1) + " " + ope + " " + str(ope2) + " = " + str(res))

    def run(self):
        # Demander les entrées à l'utilisateur
        self.math_request.ask_user_input()

        # Calculer le résultat
        result = self.math_lib.calculate(self.math_request.operand1, self.math_request.operator, self.math_request.operand2)

        # Afficher le résultat
        self.display_result(self.math_request.operand1, self.math_request.operator, self.math_request.operand2, result)

# Appeler la fonction principale pour exécuter le programme
if __name__ == "__main__":
    app = Main()
    app.run()