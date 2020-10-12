def sum_numbers(num_1, num_2):
    sum_of_nums = num_1 + num_2
    return sum_of_nums


def subtract(num1, num2):
    subtract_of_nums = num1 - num2
    return subtract_of_nums


def add_and_subtract(num1, num2, num3):
    sum_result = sum_numbers(num1, num2)
    subtract_result = subtract(sum_result, num3)
    return subtract_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
