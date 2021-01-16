numbers = [int(i) for i in input().split()]

stack = []

for num in numbers:
    stack.append(num)

while stack:
    print(stack.pop(), end=' ')