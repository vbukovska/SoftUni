circle = input().split()
turn = int(input())

flag_list = [0] * len(circle)
output_list = []
counter = 0

while flag_list.count(1) < len(circle):
    i = 0
    while i <= len(circle)-1:
        j = i
        if flag_list.count(1) == len(circle):
            break
        while j <= len(circle)-1 and counter < turn:
            if flag_list[j] == 1:
                j += 1
                if j >= len(circle):
                    i = 0
            else:
                counter += 1
                if counter == turn:
                    counter = 0
                    output_list.append(circle[j])
                    flag_list[j] = 1
                    i = j + 1
                    break
                else:
                    j += 1
                    if j >= len(circle):
                        i = 0
print('[', end='')
for num in range(len(output_list)):
    if not num == len(output_list) - 1:
        print(f'{output_list[num]},', end='')
    else:
        print(f'{output_list[num]}]')

