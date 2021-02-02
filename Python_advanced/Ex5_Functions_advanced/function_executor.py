def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for func in args:
        function = func[0]
        values = func[1]
        num1, num2 = values
        # result.append(function(*values))
        result.append(function(num1, num2))
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
