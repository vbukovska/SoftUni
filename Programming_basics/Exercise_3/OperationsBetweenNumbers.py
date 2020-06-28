number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0
parity = 'odd'
if operator == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        parity = 'even'
    print(f'{number_1} {operator} {number_2} = {result} - {parity}')
elif operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        parity = 'even'
    print(f'{number_1} {operator} {number_2} = {result} - {parity}')
elif operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        parity = 'even'
    print(f'{number_1} {operator} {number_2} = {result} - {parity}')
else:
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        if operator == '/':
            result = number_1 / number_2
            print(f'{number_1} / {number_2} = {result:.2f}')
        else:
            result = number_1 % number_2
            print(f'{number_1} % {number_2} = {result}')



