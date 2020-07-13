k = input()

total = 0

while k != 'NoMoreMoney':
    i = float(k)
    if i < 0:
        print('Invalid Operation!')
        break
    print(f'Increase: {i:.2f}')
    total += i
    k = input()

print(f'Total: {total:.2f}')
