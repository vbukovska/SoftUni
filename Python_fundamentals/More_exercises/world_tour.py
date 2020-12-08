stops = input()


def add_stop(string, index, substring):
    if 0 <= index <= len(string):
        string = string[:index] + string_to_add + string[index:]
    return string


def remove_stop(string, index_1, index_2):
    if 0 <= index_1 <= index_2 <= len(string) - 1:
        string = string[:index_1] + string[index_2+1:]
    return string


def switch(string, old_string, new_string):
    if old_string in string:
        string = string.replace(old_string, new_string)
    return string


while True:
    command_line = input()
    if command_line == 'Travel':
        break
    command, *parameters = command_line.split(':')
    if command == 'Add Stop':
        index = int(parameters[0])
        string_to_add = parameters[1]
        stops = add_stop(stops, index, string_to_add)
        print(stops)
    elif command == 'Remove Stop':
        start_index = int(parameters[0])
        end_index = int(parameters[1])
        stops = remove_stop(stops, start_index, end_index)
        print(stops)
    else:
        old_string = parameters[0]
        new_string = parameters[1]
        stops = switch(stops, old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")