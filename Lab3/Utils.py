import csv
from Student import Student

class Utils:
    def __init__(self, file_name="lab3.csv"):
        self.file_name = file_name

    def load_from_file(self):
        students = []
        try:
            with open(self.file_name, "r", newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        row.get("Name", ""),
                        row.get("Phone", ""),
                        row.get("Email", ""),
                        row.get("Group", "")
                    )
                    students.append(student)
            print(f"Data loaded from: {self.file_name}")
        except FileNotFoundError:
            print(f"File {self.file_name} not found. Creating new list.")
        return students

    def save_to_file(self, student_list):
        with open(self.file_name, "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Name", "Phone", "Email", "Group"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list:
                writer.writerow({
                    "Name": student.name,
                    "Phone": student.phone,
                    "Email": student.email,
                    "Group": student.group
                })
        print(f"Data saved to: {self.file_name}")