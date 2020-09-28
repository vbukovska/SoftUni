people = int(input())
capacity = int(input())

if people % capacity == 0:
    print(f'{people // capacity}')
else:
    print(f'{people // capacity + 1}')