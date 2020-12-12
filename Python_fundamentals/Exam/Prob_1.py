string = input()


def translate(string, char, replacement):
    if char in string:
        string = string.replace(char, replacement)
    return string


def includes(string, other_string):
    result = False
    if other_string in string:
        result = True
    return result


def start(string, other_string):
    index = string.find(other_string)
    result = False
    if index == 0:
        result = True
    return result


def remove(string, start_index, count):
    string = string[:start_index] + string[start_index + count:]
    return string


while True:
    command_line = input()
    if command_line == 'End':
        break
    command, *parameters = command_line.split(' ')
    if command == 'Translate':
        char = parameters[0]
        replacement = parameters[1]
        string = translate(string, char, replacement)
        print(string)
    elif command == 'Includes':
        other_string = parameters[0]
        print(includes(string, other_string))
    elif command == 'Start':
        other_string = parameters[0]
        print(start(string, other_string))
    elif command == 'Lowercase':
        string = string.lower()
        print(string)
    elif command == 'FindIndex':
        char = parameters[0]
        index = string.rfind(char)
        print(index)
    else:
        start_index = int(parameters[0])
        count = int(parameters[1])
        string = remove(string, start_index, count)
        print(string)