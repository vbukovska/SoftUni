strings = input().split()

while True:
    command_line = input().split()
    if command_line[0] == 'end':
        break
    command = command_line[0]
    if command == 'remove':
        number_elements = int(command_line[1])
        strings = strings[number_elements:]
    else:
        start_index = int(command_line[2])
        number_elements = int(command_line[4])
        end_index = start_index + number_elements - 1
        if command == 'reverse':
            strings = strings[:start_index] + strings[start_index:end_index + 1][::-1] + strings[end_index + 1:]
        else:
            strings = strings[:start_index] + sorted(strings[start_index:(end_index + 1)]) + strings[end_index + 1:]

print(', '.join(strings))