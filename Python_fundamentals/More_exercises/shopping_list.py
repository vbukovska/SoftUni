shopping_list = input().split('!')

while True:
    command_line = input()
    if 'Shopping!' in command_line:
        break
    if 'Correct' in command_line:
        command, old_item, new_item = command_line.split()
        if old_item in shopping_list:
            item_index = shopping_list.index(old_item)
            shopping_list[item_index] = new_item
    else:
        command, item = command_line.split()
        if command == 'Urgent':
            if item not in shopping_list:
                shopping_list.insert(0, item)
        elif command == 'Unnecessary':
            if item in shopping_list:
                shopping_list.remove(item)
        elif command == 'Rearrange':
            if item in shopping_list:
                shopping_list.remove(item)
                shopping_list.append(item)

print(', '.join(shopping_list))
