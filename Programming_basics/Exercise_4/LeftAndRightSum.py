n = int(input())

first_sum = 0
second_sum = 0

for i in range(2*n):
    number = int(input())
    if i <= n-1:
        first_sum += number
    else:
        second_sum += number
if first_sum == second_sum:
    print(f'Yes, sum = {first_sum}')
else:
    print(f'No, diff = {abs(first_sum - second_sum)}')
