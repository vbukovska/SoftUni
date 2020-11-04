numbers = [int(number) for number in input().split()]

avg_value = sum(numbers) / len(numbers)
numbers.sort(reverse=True)
result = [num for num in numbers if num > avg_value]
if len(result) == 0:
    print('No')
else:
    result = result[:5]
    print(' '.join([str(num) for num in result]))
