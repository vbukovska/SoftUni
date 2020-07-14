n = int(input())
for i in range(1111, 10000):
    number = str(i)
    sum_residuals = 0
    if '0' in number:
        continue
    for j in number:
        digit = int(j)
        if n % digit != 0:
            sum_residuals = 1
            break
    if sum_residuals == 0:
        print(f'{number}', end=' ')
