n = int(input())

number = 0
max_num = 0
min_num = 0

for i in range(n):
    number = int(input())
    if i == 0:
        max_num = number
        min_num = number
    elif number < min_num:
        min_num = number
    elif number > max_num:
        max_num = number

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')

