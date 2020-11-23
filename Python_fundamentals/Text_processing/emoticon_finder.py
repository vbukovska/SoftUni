strings = input()

for index in range(len(strings)-1):
    character = strings[index]
    if character == ':':
        symbol = strings[index + 1]
        print(f':{symbol}')

# len(curr_string.lstrip()) == len(curr_string)