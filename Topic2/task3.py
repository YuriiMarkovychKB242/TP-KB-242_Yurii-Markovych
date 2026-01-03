def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    return a / b if b != 0 else "Помилка"

a = float(input("Число 1: "))
op = input("Операція (+, -, *, /): ")
b = float(input("Число 2: "))

match op:
    case "+": print(add(a, b))
    case "-": print(subtract(a, b))
    case "*": print(multiply(a, b))
    case "/": print(divide(a, b))
    case _: print("Помилка операції")