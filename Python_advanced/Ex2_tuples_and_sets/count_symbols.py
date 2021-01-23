def custom_print(elements):
    sorted_lines = dict(sorted(elements.items(), key=lambda x: x[0]))
    for element, occurrences in sorted_lines.items():
        print(f'{element}: {occurrences} time/s')


string = input()

string_characters = {}
for char in string:
    if char not in string_characters:
        string_characters[char] = 0
    string_characters[char] += 1


custom_print(string_characters)