num = int(input())
let = int(input())

for i_1 in range(1, num+1):
    for i_2 in range(1, num+1):
        for i_3 in range(97, 97+let):
            for i_4 in range(97, 97+let):
                for i_5 in range(max(i_1, i_2)+1, num+1):
                    print(f'{str(i_1)+str(i_2)+chr(i_3)+chr(i_4)+str(i_5)}', end=' ')
