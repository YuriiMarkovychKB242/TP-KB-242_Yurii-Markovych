def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0: return "Помилка"
    return a / b

a = float(input("Число 1: "))
op = input("Операція (+, -, *, /): ")
b = float(input("Число 2: "))

if op == "+": print(f"Результат: {add(a, b)}")
elif op == "-": print(f"Результат: {subtract(a, b)}")
elif op == "*": print(f"Результат: {multiply(a, b)}")
elif op == "/": print(f"Результат: {divide(a, b)}")
else: print("Помилка операція")