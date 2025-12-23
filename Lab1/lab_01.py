# already sorted list
list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-241"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@gmail.com", "group": "KB-241"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@gmail.com", "group": "KB-242"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@ukr.net", "group": "KB-242"}
]

def printAllList():
    """Друк списку з усіма 4 полями """
    print("-" * 60)
    for elem in list:
        strForPrint = (f"Name: {elem['name']:<10} | Phone: {elem['phone']:<12} | "
                       f"Email: {elem['email']:<15} | Group: {elem['group']}")
        print(strForPrint)
    print("-" * 60)
    return

def addNewElement():
    """Додавання нового елемента зі збереженням сортування """
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    
    # щоб список залишався відсортованим 
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
            
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    """Видалення елемента за ім'ям"""
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
            
    if deletePosition == -1:
        print("Element was not found")
    else:
        print(f"Deleting student: {list[deletePosition]['name']}")
        del list[deletePosition]
    return


def updateElement():
    """Оновлення інформації про студента"""
    name = input("Please enter name to be updated: ")
    updateIndex = -1
    
    # Пошук існуючого запису
    for index, item in enumerate(list):
        if item["name"] == name:
            updateIndex = index
            break
            
    if updateIndex == -1:
        print("Student not found")
    else:
        print(f"Updating data for {name}.")
        
        # Отримуємо нові дані або залишаємо старі
        new_name = input(f"New name ({list[updateIndex]['name']}): ") or list[updateIndex]['name']
        new_phone = input(f"New phone ({list[updateIndex]['phone']}): ") or list[updateIndex]['phone']
        new_email = input(f"New email ({list[updateIndex]['email']}): ") or list[updateIndex]['email']
        new_group = input(f"New group ({list[updateIndex]['group']}): ") or list[updateIndex]['group']
        
        # Видаляємо старий запис та додаємо новий через addNewElement для збереження сортування 
        del list[updateIndex]
        
        newItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
        
        insertPosition = 0
        for item in list:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
        list.insert(insertPosition, newItem)
        print("Element has been updated")

def main():
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
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()