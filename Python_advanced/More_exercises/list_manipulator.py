def list_manipulator(numbers, *args):
    action_command, position_command, *values = args
    if action_command == "add":
        if position_command == "beginning":
            while values:
                value = values.pop()
                numbers.insert(0, value)
        else:
            numbers.extend(values)
    else:
        if action_command == "remove":
            if position_command == "beginning":
                if values:
                    value = values[0]
                else:
                    value = 1
                for num in range(value):
                    numbers.pop(0)
            else:
                if values:
                    value = values[0]
                else:
                    value = 1
                for num in range(value):
                    numbers.pop()
    return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
