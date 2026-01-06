import functions

def get_data():
    a = float(input("Число 1: "))
    b = float(input("Число 2: "))
    op = input("Оберіть операцію (+, -, *, /) або 'x': ")
    return a, b, op

def execute_operation(a, b, op):
    if op == "+": return functions.add(a, b)
    elif op == "-": return functions.sub(a, b)
    elif op == "*": return functions.mult(a, b)
    elif op == "/": return functions.div(a, b)
    return "Помилка операції"