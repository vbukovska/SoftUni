def exists(item, list_items):
    return item in list_items


collection = input().split(', ')

while True:
    command, *items = input().split(' - ')
    if command == 'Craft!':
        break
    if command == 'Combine Items':
        old_item, new_item = items[0].split(':')
        if exists(old_item, collection):
            collection.insert(collection.index(old_item) + 1, new_item)
    elif command == 'Collect':
        if not exists(items[0], collection):
            collection.append(items[0])
    elif command == 'Drop':
        if exists(items[0], collection):
            collection.remove(items[0])
    elif command == 'Renew':
        if exists(items[0], collection):
            collection.remove(items[0])
            collection.append(items[0])

print(', '.join(collection))
