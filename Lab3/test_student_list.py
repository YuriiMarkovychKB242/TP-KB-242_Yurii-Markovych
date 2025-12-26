import unittest
from Student import Student
from StudentList import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.sl = StudentList()
        self.student1 = Student("Ivan", "123", "ivan@test.com", "IP-22")
        self.student2 = Student("Anna", "456", "anna@test.com", "IP-22")

    def test_add_student_sorted(self):
        # Додавання без сортування порядку щоб перевірити сортування
        self.sl.add_student(self.student1) # Ivan
        self.sl.add_student(self.student2) # Anna
        
        # Anna повинна бути першою 
        self.assertEqual(self.sl.students[0].name, "Anna")
        self.assertEqual(self.sl.students[1].name, "Ivan")

        # перевірка видалення
    def test_delete_student(self):
        self.sl.add_student(self.student1)
        self.sl.delete_student("Ivan")
        self.assertEqual(len(self.sl.students), 0)

    def test_update_student(self):
        self.sl.add_student(self.student1)
        new_student = Student("IvanNew", "999", "new@test.com", "IP-23")
        self.sl.update_student("Ivan", new_student)
        
        self.assertEqual(self.sl.students[0].name, "IvanNew")
        self.assertEqual(self.sl.students[0].phone, "999")
        self.assertEqual(self.sl.students[0].group, "IP-23")

if __name__ == '__main__':
    unittest.main()