message = input().split()
result_phrase = []
for word in message:
    letters = list(word)
    first_letter = [num for num in letters if num.isnumeric()]
    letters = [el for el in letters if el not in first_letter]
    letters[0], letters[-1] = letters[-1], letters[0]
    letters.insert(0, chr(int(''.join(first_letter))))
    result_phrase.extend(letters)
    result_phrase.append(' ')
print(''.join(result_phrase))