import csv
from sys import argv

#список студентів
student_list = []

#завантаження студентів
def load_data(file_name):
    global student_list
    try:
        with open(file_name, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # якщо менше полів ніж у програмі
                student_list.append({
                    "name": row.get("Name", ""),
                    "phone": row.get("Phone", ""),
                    "email": row.get("Email", ""),
                    "group": row.get("Group", "")
                })
        print(f"Завантажено данні з: {file_name}")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено")

#зберігання списку
def save_data(file_name):
    with open(file_name, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Name", "Phone", "Email", "Group"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_list:
            writer.writerow({
                "Name": student["name"],
                "Phone": student["phone"],
                "Email": student["email"],
                "Group": student["group"]
            })
    print(f"Збережено до: {file_name}")

def printAllList():
    print("-" * 60)
    for elem in student_list:
        strForPrint = (f"Name: {elem['name']:<10} | Phone: {elem['phone']:<12} | "
                       f"Email: {elem['email']:<15} | Group: {elem['group']}")
        print(strForPrint)
    print("-" * 60)

#Логічні функції

def add_item_to_list(name, phone, email, group):
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in student_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    student_list.insert(insertPosition, newItem)
    return insertPosition

def delete_item_from_list(name):
    for item in student_list:
        if name == item["name"]:
            student_list.remove(item)
            return True
    return False

def update_item_in_list(name, new_name, new_phone, new_email, new_group):
    # видалити старий запис
    if delete_item_from_list(name):
        # Додати новий запич
        add_item_to_list(new_name, new_phone, new_email, new_group)
        return True
    return False

#інтерфейс

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    add_item_to_list(name, phone, email, group)
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    if delete_item_from_list(name):
        print(f"Student {name} deleted")
    else:
        print("Element was not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    current_student = None
    for item in student_list:
        if item["name"] == name:
            current_student = item
            break
            
    if current_student:
        print(f"Updating data for {name}.")
        new_name = input(f"New name ({current_student['name']}): ") or current_student['name']
        new_phone = input(f"New phone ({current_student['phone']}): ") or current_student['phone']
        new_email = input(f"New email ({current_student['email']}): ") or current_student['email']
        new_group = input(f"New group ({current_student['group']}): ") or current_student['group']
        
        update_item_in_list(name, new_name, new_phone, new_email, new_group)
        print("Element has been updated")
    else:
        print("Student not found")

def main():
    if len(argv) > 1:
        file_name = argv[1]
        load_data(file_name)
    else:
        file_name = "lab2.csv" # Файл для збереження

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match chouse:
            case "C" | "c":
                addNewElement()
            case "U" | "u":
                updateElement()
            case "D" | "d":
                deleteElement()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                save_data(file_name) # Збереження при виході
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()