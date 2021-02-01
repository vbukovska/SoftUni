nums = [int(n) for n in input().split()]

print(list(filter(lambda x: x % 2 == 0, nums)))