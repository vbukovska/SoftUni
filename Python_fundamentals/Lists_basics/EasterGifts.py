gifts = input().split()
command = input()

while not command == 'No Money':
    commands = command.split()
    if commands[0] == 'OutOfStock':
        while commands[1] in gifts:
            gifts[gifts.index(commands[1])] = None
    elif commands[0] == 'Required' and 0 < int(commands[2]) <= len(gifts) - 1:
        gifts[int(commands[2])] = commands[1]
    else:
        gifts[-1] = commands[1]
    command = input()

for element in gifts:
    if element is not None:
        print(element, end=' ')