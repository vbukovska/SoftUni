n = int(input())

n1 = 0
n2 = 0
n3 = 0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        n1 += 1
    if number % 3 == 0:
        n2 += 1
    if number % 4 == 0:
        n3 += 1

print(f'{(n1 / n) * 100:.2f}%')
print(f'{(n2 / n) * 100:.2f}%')
print(f'{(n3 / n) * 100:.2f}%')
