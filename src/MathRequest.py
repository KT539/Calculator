class MathRequest:
    def ask_user_float_input(self, float_input):
        while True:
            try:
                return float(input(float_input))
            except ValueError:
                print("Please enter a float.")

    def ask_user_input(self):
        # Demander à l'utilisateur d'entrer les valeurs
        self.operand1 = self.ask_user_float_input("Enter the first operand: ")
        self.operator = input("Enter an operator (+, -, *, **, /): ")
        self.operand2 = self.ask_user_float_input("Enter the second operand: ")