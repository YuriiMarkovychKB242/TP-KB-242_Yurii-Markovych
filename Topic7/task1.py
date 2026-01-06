class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Створення списку
students = [
    Student("Andriy", 21),
    Student("Maria", 19),
    Student("Oksana", 22),
    Student("Ihor", 20)
]

# Сортування списку за допомогою sorted
sorted_students = sorted(students, key=lambda student: student.age)

print("Sorted Students by Age")
for s in sorted_students:
    print(s)