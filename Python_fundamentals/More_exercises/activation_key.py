activation_key = input()


def flip(string, flip_to, start, end):
    substring = string[start:end]

    if flip_to == 'Upper':
        substring = substring.upper()
    else:
        substring = substring.lower()

    string = string[:start] + substring + string[end:]
    return string


def slice(string, start, end):
    substring = string[:start] + string[end:]
    return substring


def contains(string, substring):
    if substring in string:
        return f"{string} contains {substring}"
    else:
        return "Substring not found!"


while True:
    command = input()
    if command == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break
    commands = command.split('>>>')
    if len(commands) == 2:
        substring = commands[1]
        print(contains(activation_key, substring))
    elif len(commands) == 4:
        flip_to = commands[1]
        start = int(commands[2])
        end = int(commands[3])
        activation_key = flip(activation_key, flip_to, start, end)
        print(activation_key)
    elif len(commands) == 3:
        start = int(commands[1])
        end = int(commands[2])
        activation_key = slice(activation_key, start, end)
        print(activation_key)