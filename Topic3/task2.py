# Початковий список для тестування
fruits = ["apple", "banana", "cherry"]
print(f"Початковий список: {fruits}")

# 1. append() - додає елемент в кінець списку
fruits.append("orange")
print(f"Після append: {fruits}")

# 2. extend() - додає елементи іншого списку в кінець
more_fruits = ["kiwi", "lemone"]
fruits.extend(more_fruits)
print(f"Після extend: {fruits}")

# 3. insert() - вставляє елемент на вказану позицію
# mango на першу позицію
fruits.insert(1, "mango")
print(f"Після insert: {fruits}")

# 4. remove() - видаляє перший знайдений елемент із вказаним значенням
fruits.remove("banana")
print(f"Після remove: {fruits}")

# 5. copy() - створює поверхневу копію списку
fruits_copy = fruits.copy()
print(f"Копія списку: {fruits_copy}")

# 6. reverse() - розгортає список у зворотному порядку
fruits.reverse()
print(f"Після reverse(): {fruits}")

# 7. sort() - сортує список за замовчуванням за алфавітом
fruits.sort()
print(f"Після sort(): {fruits}")

# 8. clear() - повністю очищує список
fruits.clear()
print(f"Після clear(): {fruits}")