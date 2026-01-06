students = [
    {"name": "Ihor", "grade": 95},
    {"name": "Vova", "grade": 88},
    {"name": "Katya", "grade": 92},
    {"name": "Maria", "grade": 100}
]

# Сортування за ім'ям 
sorted_by_name = sorted(students, key=lambda x: x['name'])

# Сортування за оцінкою 
sorted_by_grade = sorted(students, key=lambda x: x['grade'])

print("Sorted by Name:", sorted_by_name)
print("Sorted by Grade:", sorted_by_grade)