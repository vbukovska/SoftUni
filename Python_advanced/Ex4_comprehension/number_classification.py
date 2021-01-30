numbers = [int(num) for num in input().split(', ')]
positive_nums = [num for num in numbers if num >= 0]

even_nums = [num for num in numbers if num % 2 == 0]


print('Positive:', end=' ')
print(', '.join(str(n) for n in positive_nums))

print('Negative:', end=' ')
print(', '.join(str(n) for n in numbers if n not in positive_nums))

print('Even:', end=' ')
print(', '.join(str(n) for n in even_nums))

print('Odd:', end=' ')
print(', '.join(str(n) for n in numbers if n not in even_nums))


