number_to_check = int(input())


def is_perfect_number(number):
    sum_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_divisors += divisor
    if 0 < number == sum_divisors:
        return ' We have a perfect number!'
    else:
        return "It's not so perfect."


result = is_perfect_number(number_to_check)
print(result)