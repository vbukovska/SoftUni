message = input()


def insert_space(string, index):
    result_string = string[:index] + ' ' + string[index:]
    return result_string


def reverse(string, substring):
    string = string.replace(substring, '', 1)
    substring = substring[::-1]
    string = string + substring
    return string


def change_all(string, substring, replacement):
    string = string.replace(substring, replacement)
    return string


while True:
    command = input()
    if command == 'Reveal':
        break
    command = command.split(':|:')
    if command[0] == 'InsertSpace':
        index = int(command[1])
        message = insert_space(message, index)
        print(message)
    elif command[0] == 'Reverse':
        substring = command[1]
        index = message.find(substring)
        if not index == -1:
            message = reverse(message, substring)
            print(message)
        else:
            print('error')
    else:
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)
        print(message)

print(f"You have a new text message: {message}")
