def filter_nums(nums, command):
    if command == "odd":
        result = list(filter(lambda x: not x % 2 == 0, nums))
    else:
        result = list(filter(lambda x: x % 2 == 0, nums))
    return result


def even_odd(*args):
    command = args[-1]
    nums = filter_nums(args[:-1], command)
    return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))