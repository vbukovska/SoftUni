inventory = input().split(', ')


while True:
    command_line = input().split(' - ')
    command = command_line[0]
    if command == 'Craft!':
        print(', '.join(inventory))
        break
    item = command_line[1]
    if command == 'Collect' and item not in inventory:
        inventory.append(item)
    elif command == 'Drop' and item in inventory:
        inventory.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in inventory:
            inventory.insert(inventory.index(old_item)+1, new_item)
    elif item in inventory:
        inventory.remove(item)
        inventory.append(item)

