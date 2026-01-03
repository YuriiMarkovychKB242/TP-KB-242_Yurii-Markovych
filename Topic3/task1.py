def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Помилка"

while True:
    print("Калькулятор (введіть 'x' для виходу)")
    op = input("Оберіть операцію (+, -, *, /) або 'x': ")
    
    if op.lower() == 'x':
        print("Програму завершено.")
        break
        
    if op not in ('+', '-', '*', '/'):
        print("Невідома операція!")
        continue

    try:
        a = float(input("Число 1: "))
        b = float(input("Число 2: "))
        
        match op:
            case "+": print(f"Результат: {add(a, b)}")
            case "-": print(f"Результат: {sub(a, b)}")
            case "*": print(f"Результат: {mult(a, b)}")
            case "/": print(f"Результат: {div(a, b)}")
    except ValueError:
        print("Помилка операції")