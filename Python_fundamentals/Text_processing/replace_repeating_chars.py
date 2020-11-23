string = input()
result_string = ''
curr_char = ''
for char in string:
    if not char == curr_char:
        curr_char = char
        result_string += char

print(result_string)