n = int(input())
for i_1 in range(1, 10):
    if n % i_1 == 0:
        for i_2 in range(1, 10):
            if n % i_2 == 0:
                for i_3 in range(1, 10):
                    if n % i_3 == 0:
                        for i_4 in range(1, 10):
                            if n % i_4 == 0:
                                print(str(i_1)+str(i_2)+str(i_3)+str(i_4), end=' ')
