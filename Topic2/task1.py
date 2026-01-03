import math

def get_discriminant(a, b, c):
    return b**2 - 4*a*c

def solve_quadratic(a, b, c):
    d = get_discriminant(a, b, c)
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Два корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2*a)
        return f"Один корінь: x = {x}"
    else:
        return "Коренів немає (D < 0)"

# Приклад використання
print(solve_quadratic(1, -5, 6))