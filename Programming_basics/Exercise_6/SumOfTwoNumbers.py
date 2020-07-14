start = int(input())
end = int(input())
magic_number = int(input())

flag = False


for i in range(start, end+1):
    for j in range(start, end+1):
        if i + j == magic_number:
            flag = True
            print(f'Combination N:{(i-start+1)*(j-start+1)} ({i} + {j} = {magic_number})')
            break
    if flag:
        break
if not flag:
    print(f'{(end - start +1)**2} combinations - neither equals {magic_number}')
