n1 = int(input())
n2 = int(input())
for i in range(n1, n2+1):
    num = str(i)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(num):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(i, end=' ')
