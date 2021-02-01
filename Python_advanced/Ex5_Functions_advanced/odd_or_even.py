def filter_nums(nums, command):
    if command == "Odd":
        result = list(filter(lambda x: not x % 2 == 0, nums))
    else:
        result = list(filter(lambda x: x % 2 == 0, nums))
    return result


def print_result(nums, command):
    if command == 'Odd':
        filtered_nums = filter_nums(nums, command)
    else:
        filtered_nums = filter_nums(nums, command)
    sum_nums = sum(filtered_nums)
    return sum_nums * len(nums)


command = input()
nums = [int(n) for n in input().split()]

print(print_result(nums, command))