import re
string = input()
# pattern = r"(?P<delimiter>#|@)(?P<word>[a-zA-Z][a-zA-Z][a-zA-Z]+)\1"
# pattern = r"(((#|@)([a-zA-Z]{3,})\3){2})"
# pattern = r"(?P<pair>((?P<delimiter>\3|(#|@))([a-zA-Z]{3,})\3){2})"
pattern = r"(?P<pair>(?P<delimiter>#|@)([a-zA-Z]{3,})\2{2}([a-zA-Z]{3,})\2)"
mirror_words = []
words = re.finditer(pattern, string)
pairs = [word.groupdict() for word in words]
if len(pairs) == 0:
    print('No word pairs found!')
else:
    print(f"{len(pairs)} word pairs found!")
for curr_pair in pairs:
    delimiter = curr_pair['delimiter']
    splited_pair = curr_pair['pair'].split(delimiter)
    splited_pair = [x for x in splited_pair if x]
    first_word = splited_pair[0]
    second_word = splited_pair[1]
    if first_word == second_word[::-1]:
        mirror_words.append({'first_word': first_word, 'second_word': second_word})
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join([mirror_pair['first_word'] + ' <=> ' + mirror_pair['second_word'] for mirror_pair in mirror_words]))
