from functools import reduce


def operate(operator, *args):
    if operator == '+':
        result = reduce(lambda x, y: x + y, args)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, args)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, args)
    else:
        result = reduce(lambda x, y: x / y, args)
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))