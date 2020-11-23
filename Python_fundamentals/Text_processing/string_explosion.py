string = input()
result_string = ''
chars_to_del = 0
is_power = False
for char_index in range(len(string)):
    curr_char = string[char_index]
    if curr_char == '>':
        is_power = True
        result_string += curr_char
    else:
        if is_power:
            chars_to_del += int(curr_char)
            is_power = False
        if chars_to_del > 0:
            chars_to_del -= 1
        else:
            result_string += curr_char

print(result_string)