num = input()


def odd_even_sum(number, sum_type):
    result_sum = 0
    for digit in number:
        int_num = int(digit)
        if sum_type == 'even' and int_num % 2 == 0:
            result_sum += int_num
        elif sum_type == 'odd' and not int_num % 2 == 0:
            result_sum += int_num
    return result_sum


print(f'Odd sum = {odd_even_sum(num,"odd")}, Even sum = {odd_even_sum(num, "even")}')
