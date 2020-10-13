first_number = int(input())
second_number = int(input())


def calculate_factoriel(number):
    result = 1
    while number > 0:
        result = result * number
        number = number - 1
    return result


final_result = calculate_factoriel(first_number) / calculate_factoriel(second_number)
print(f'{final_result:.2f}')

