text = input()

result_text = ''

for character in text:
    old_character_ascii = ord(character)
    new_character = chr(old_character_ascii + 3)
    result_text += new_character

print(result_text)
