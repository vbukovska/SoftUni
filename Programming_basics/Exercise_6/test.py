start = int(input())
end = int(input())
magic_number = int(input())

flag = False
counter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            flag = True
            print(f'Combination N: {counter} ({i} + {j} = {magic_number})')
            break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magic_number}')
