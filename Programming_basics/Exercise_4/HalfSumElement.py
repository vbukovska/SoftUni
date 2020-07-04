n = int(input())

max_num = 0
total = 0
for i in range(n):
    number = int(input())
    if i == 0 or number > max_num:
        max_num = number
    total += number

if max_num == total - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - (total - max_num))}')
