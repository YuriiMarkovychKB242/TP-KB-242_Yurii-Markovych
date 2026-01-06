from functions import CalculatorLogic

class CalculatorInterface:
    def __init__(self):
        self.logic = CalculatorLogic()

    def get_data(self):
        try:
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            op = input("Оберіть операцію (+, -, *, /) або 'x': ")
            return a, b, op
        except ValueError:
            print("Error")
            return None

    def process(self):
        data = self.get_data()
        if not data: return
        
        a, b, op = data
        try:
            if op == '+': res = self.logic.add(a, b)
            elif op == '-': res = self.logic.sub(a, b)
            elif op == '*': res = self.logic.mult(a, b)
            elif op == '/': res = self.logic.div(a, b)
            else: 
                print("Помилка операції")
                return
            print(f"Result: {res}")
        except ZeroDivisionError as e:
            print(e)