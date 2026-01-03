def add(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b

def div(a, b):
    # Обробка виняткової ситуації ділення на нуль 
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль неможливе!"

def get_number(prompt):
    # Функція запиту даних, що обробляє помилки введення 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено не число.")

while True:
    print("Калькулятор (введіть 'x' для виходу)")
    op = input("Оберіть операцію (+, -, *, /) або 'x': ")
    
    if op.lower() == 'x':
        break
        
    if op not in ('+', '-', '*', '/'):
        print("Невідома операція!")
        continue

    # Отримання чисел через захищену функцію 
    a = get_number("Число 1: ")
    b = get_number("Число 2: ")
    
    match op:
        case "+": print(f"Результат: {add(a, b)}")
        case "-": print(f"Результат: {sub(a, b)}")
        case "*": print(f"Результат: {mult(a, b)}")
        case "/": print(f"Результат: {div(a, b)}")