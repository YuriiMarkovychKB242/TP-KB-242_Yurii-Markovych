from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        # вставка із сортуванням по імені
        insert_position = 0
        for item in self.students:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        print(f"Student {student.name} added.")

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted.")
                return True
        print("Element was not found.")
        return False

    def update_student(self, name, new_student: Student):
        # видалити старий, додати новий щоб зберегти сортування
        if self.delete_student(name):
            self.add_student(new_student)
            print("Element has been updated.")
            return True
        return False

    def get_all_students(self):
        return self.students
    
    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None