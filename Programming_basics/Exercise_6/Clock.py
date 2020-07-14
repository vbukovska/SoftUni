for i in range(0, 24):
    for j in range(0, 60):
        print(f'{i}:{j}')


for i in range(0, 24):
    for j in range(0, 60):
        if i <= 9:
            if j <= 9:
                print(f'0{i}:0{j}')
            else:
                print(f'0{i}:{j}')
        else:
            if j <= 9:
                print(f'{i}:0{j}')
            else:
                print(f'{i}:{j}')