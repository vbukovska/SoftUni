numbers = [int(num) for num in input().split(', ')]

# groups = max(numbers) // 10 + 1 * min(max(numbers) % 2, 1)
#
# for group in range(1, groups + 1):
#     group_list = [num for num in numbers if num <= group * 10]
#     numbers = [num for num in numbers if num not in group_list]
#     print(f'Group of {group * 10}\'s: {group_list}')

group = 10
while len(numbers) > 0:
    group_list = list(filter(lambda x: x <= group, numbers))
    numbers = [num for num in numbers if num not in group_list]
    print(f'Group of {group}\'s: {group_list}')
    group += 10
