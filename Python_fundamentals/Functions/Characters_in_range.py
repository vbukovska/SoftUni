def chars_in_ascii_range(char_1, char_2):
    range_list = range(ord(char_1)+1, ord(char_2))
    result_list = [chr(x) for x in range_list]
    return result_list


character_1 = input()
character_2 = input()
char_list = chars_in_ascii_range(character_1, character_2)
for char in char_list:
    print(char, end=' ')
