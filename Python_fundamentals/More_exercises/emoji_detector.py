import re


def prod(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


string = input()

digits = re.finditer(r"\d", string)
digits = [int(d.group()) for d in digits]

cool_treshold = prod(digits)

pattern = r"(?P<separator>\*|:){2}(?P<emoticon>[A-Z][a-z][a-z]+)\1{2}"
emoticon = re.finditer(pattern, string)
emoticon = [e.groupdict() for e in emoticon]

count_emoticons = len(emoticon)
print(f"Cool threshold: {cool_treshold}")
print(f"{count_emoticons} emojis found in the text. The cool ones are:")
for emoji in emoticon:
    sum_chars = 0
    emo = emoji['emoticon']
    separator = emoji['separator'] * 2
    for char in emo:
        sum_chars += ord(char)
    if sum_chars >= cool_treshold:
        print(f"{separator}{emo}{separator}")


