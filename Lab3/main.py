from sys import argv
from Student import Student
from StudentList import StudentList
from Utils import Utils

def main():
    file_name = "lab3.csv"
    if len(argv) > 1:
        file_name = argv[1]

    student_list = StudentList()
    file_handler = Utils(file_name)

    # Завантаження даних
    loaded_data = file_handler.load_from_file()
    # Щоб зберегти порядок
    student_list.students = loaded_data 

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        
        if choice.lower() == 'c':
            name = input("Please enter student name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            group = input("Please enter student group: ")
            student_list.add_student(Student(name, phone, email, group))
            
        elif choice.lower() == 'u':
            name = input("Please enter name to be updated: ")
            # пошук студента
            current = student_list.find_student(name)
            
            if current:
                print(f"Updating data for {name}.")
                new_name = input(f"New name ({current.name}): ") or current.name
                new_phone = input(f"New phone ({current.phone}): ") or current.phone
                new_email = input(f"New email ({current.email}): ") or current.email
                new_group = input(f"New group ({current.group}): ") or current.group
                
                # Оновлення данних списку
                student_list.update_student(name, Student(new_name, new_phone, new_email, new_group))
            else:
                print("Student not found")

        elif choice.lower() == 'd':
            name = input("Please enter name to be deleted: ")
            student_list.delete_student(name)
            
        elif choice.lower() == 'p':
            print("-" * 60)
            for student in student_list.get_all_students():
                print(student)
            print("-" * 60)
            
        elif choice.lower() == 'x':
            file_handler.save_to_file(student_list.get_all_students())
            print("Exit()")
            break
            
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()