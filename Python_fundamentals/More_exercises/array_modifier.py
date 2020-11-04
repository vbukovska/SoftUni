elements = [int(el) for el in input().split()]

while True:
    command_line = input()
    if command_line == 'end':
        break
    command, *indexes = command_line.split()
    if command == 'decrease':
        elements = [el - 1 for el in elements]
    else:
        index_1 = int(indexes[0])
        index_2 = int(indexes[1])
        if command == 'swap':
            elements[index_1], elements[index_2] = elements[index_2], elements[index_1]
        elif command == 'multiply':
            elements[index_1] *= elements[index_2]
print(', '.join([str(el) for el in elements]))
