string = input()
number_to_repeat = ''
result_string = ''
curr_character = ''
for index, character in enumerate(string):
    if character.isnumeric():
        number_to_repeat += character
        if index == len(string) - 1:
            result_string += curr_character * int(number_to_repeat)
    else:
        if not number_to_repeat == '':
            result_string += curr_character * int(number_to_repeat)
            curr_character = ''
            number_to_repeat = ''
        if character.isalpha() and character.islower():
            curr_character += character.capitalize()
        else:
            curr_character += character

print(f"Unique symbols used: {len(set(result_string))}")
print(result_string)
