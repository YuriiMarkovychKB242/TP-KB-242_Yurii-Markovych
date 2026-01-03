def calculate_discriminant(a, b, c):
    """Функція пошуку дискримінанту квадратного рівняння """
    discriminant = b**2 - 4 * a * c
    return discriminant

# Приклад тестування
a, b, c = 1, -5, 6
result = calculate_discriminant(a, b, c)
print(f"Для рівняння з a={a}, b={b}, c={c} дискримінант D = {result}")