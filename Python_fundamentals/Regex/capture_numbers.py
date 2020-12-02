import re

pattern = r"(\d+)"
numbers = []
data = input()
while data:
    numbers.extend(re.finditer(pattern, data))
    data = input()

numbers = [n.group() for n in numbers]
print(*numbers)