import unittest
from unittest.mock import patch
from src.MathRequest import MathRequest

class TestMathRequest(unittest.TestCase):

    @patch('builtins.input', side_effect=['3.5', '+', '2.5'])  # Simule les entrées de l'utilisateur
    def test_ask_user_input(self, mock_input):
        # Crée une instance de MathRequest
        math_request = MathRequest()

        # Appelle la méthode ask_user_input() pour tester le comportement
        math_request.ask_user_input()

        # Vérifie que les valeurs ont été correctement assignées
        self.assertEqual(math_request.operand1, 3.5)
        self.assertEqual(math_request.operator, '+')
        self.assertEqual(math_request.operand2, 2.5)

    @patch('builtins.input', side_effect=['a', '3.5', '+', '2.5'])
    def test_ask_user_float_input_invalid(self, mock_input):
        # Crée une instance de MathRequest
        math_request = MathRequest()

        # Teste la fonction ask_user_float_input() avec une valeur invalide
        # La première entrée sera incorrecte (chaîne 'a'), donc la fonction demandera à nouveau une entrée correcte.
        result = math_request.ask_user_float_input("Enter a float: ")

        # Vérifie que la fonction a bien récupéré 3.5 après la deuxième entrée valide
        self.assertEqual(result, 3.5)

if __name__ == '__main__':
    unittest.main()