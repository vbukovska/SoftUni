string = input()


def take_odd(string):
    result_string = ''
    for index in range(1, len(string), 2):
        result_string += string[index]
    return result_string


def cut(string, index, length):
    part = string[index:(index + length)]
    string = string.replace(part, '', 1)
    return string


while True:
    command = input()
    if command == "Done":
        break
    command = command.split()
    if command[0] == 'TakeOdd':
        string = take_odd(string)
        print(string)
    elif 'Cut' in command:
        index = int(command[1])
        length = int(command[2])
        string = cut(string, index, length)
        print(string)
    else:
        substring = command[1]
        replacement = command[2]
        if substring in string:
            string = string.replace(substring, replacement)
            print(string)
        else:
            print('Nothing to replace!')


print(f"Your password is: {string}")