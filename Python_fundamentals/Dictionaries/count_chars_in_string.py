text = list(input())

occurances = {}

for char in text:
    occurance = text.count(char)
    occurances[char] = occurance

if ' ' in occurances:
    occurances.pop(' ')

for key, value in occurances.items():
    print(f"{key} -> {value}")
