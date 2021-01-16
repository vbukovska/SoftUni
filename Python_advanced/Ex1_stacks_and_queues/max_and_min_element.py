steps = int(input())
push = '1'
delete = '2'
print_max = '3'
print_min = '4'

numbers_stack = []
maximum_stack = []
minimum_stack = []


for _ in range(steps):
    command_line = input().split()
    command = command_line[0]
    if command == push:
        number_to_add = int(command_line[1])
        if not numbers_stack:
            numbers_stack.append(number_to_add)
            maximum_stack.append(number_to_add)
            minimum_stack.append(number_to_add)
        else:
            current_max = maximum_stack[-1]
            current_min = minimum_stack[-1]
            numbers_stack.append(number_to_add)
            if number_to_add > current_max:
                maximum_stack.append(number_to_add)
            else:
                maximum_stack.append(current_max)
            if number_to_add < current_min:
                minimum_stack.append(number_to_add)
            else:
                minimum_stack.append(current_min)
    elif command == delete:
        if numbers_stack:
            numbers_stack.pop()
            minimum_stack.pop()
            maximum_stack.pop()
    elif command == print_max:
        if maximum_stack:
            print(maximum_stack[-1])
    elif command == print_min:
        if minimum_stack:
            print(minimum_stack[-1])

print(', '.join([str(numbers_stack.pop()) for _ in range(len(numbers_stack))]))
