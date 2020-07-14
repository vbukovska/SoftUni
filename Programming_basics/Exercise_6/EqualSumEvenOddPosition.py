num_1 = int(input())
num_2 = int(input())

for i in range(num_1, num_2+1):
    number = str(i)
    even_sum = 0
    odd_sum = 0
    for j in range(0, 6):
        if j % 2 == 0:
            even_sum += int(number[j])
        else:
            odd_sum += int(number[j])
    if even_sum == odd_sum:
        print(i, end=' ')
