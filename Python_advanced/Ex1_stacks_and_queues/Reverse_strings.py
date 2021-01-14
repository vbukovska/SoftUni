string = input()

reversed_string = ''
stack = []

for index in range(len(string)):
    stack.append(string[index])

while stack:
    reversed_string += stack.pop()

print(reversed_string)