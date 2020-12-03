import re

sentence = input()
word = input().lower()

# pattern = r"(^|(?<=\s))[a-z']+($|(?=[\s,\.!\?:;\"'/-] ?))"
# pattern = r"(^|(?<=\s))[\w']+($|(?=[^\w] ?))"
# pattern = r"\b[a-z]+('[a-z]+)?\b"
pattern = f'\\b{word}\\b'
words = re.finditer(pattern, sentence, re.IGNORECASE)

words = [w.group().lower()for w in words]

word_accurances = words.count(word)

print(word_accurances)