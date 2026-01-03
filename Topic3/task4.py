def find_insert_position(sorted_list, new_element):
    position = 0
    for i, val in enumerate(sorted_list):
        if new_element > val:
            position = i + 1
        else:
            break
    return position

my_list = [10, 20, 30, 40, 50]
elem = 35
pos = find_insert_position(my_list, elem)
print(f"Позиція для вставки {elem} у {my_list}: індекс {pos}")