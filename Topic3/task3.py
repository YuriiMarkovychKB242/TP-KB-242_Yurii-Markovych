student = {"name": "Ihor", "age": 20}

student.update({"city": "Kyiv", "age": 21})
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

del student["age"]
student.clear()
print(f"Після очищення: {student}")