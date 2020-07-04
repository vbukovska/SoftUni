n = int(input())

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(n):
    number = int(input())
    if number < 200:
        n1 += 1
    elif number <= 399:
        n2 += 1
    elif number <= 599:
        n3 += 1
    elif number <= 799:
        n4 += 1
    else:
        n5 += 1
print(f'{(n1 / n)*100:.2f}%')
print(f'{(n2 / n)*100:.2f}%')
print(f'{(n3 / n)*100:.2f}%')
print(f'{(n4 / n)*100:.2f}%')
print(f'{(n5 / n)*100:.2f}%')
