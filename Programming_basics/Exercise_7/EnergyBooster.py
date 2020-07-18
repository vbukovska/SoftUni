fruit = input()
size = input()
n = int(input())

total = 0

if fruit == 'Watermelon':
    if size == 'small':
        total += 2 * n * 56
    else:
        total += 5 * n * 28.7
elif fruit == 'Mango':
    if size == 'small':
        total += 2 * n * 36.66
    else:
        total += 5 * n * 19.6
elif fruit == 'Pineapple':
    if size == 'small':
        total += 2 * n * 42.10
    else:
        total += 5 * n * 24.80
else:
    if size == 'small':
        total += 2 * n * 20
    else:
        total += 5 * n * 15.20

if total > 1000:
    total = total - total * 0.5
elif total >= 400:
    total = total - total * 0.15
print(f'{total:.2f} lv.')