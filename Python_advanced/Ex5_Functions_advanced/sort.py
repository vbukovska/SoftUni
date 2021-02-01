nums = [int(n) for n in input().split()]

sorted_nums = sorted(nums, key=lambda x: x)
print(sorted_nums)