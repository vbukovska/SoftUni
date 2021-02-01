from functools import reduce


def expressions(nums, operants=[], i=1, j=0, step=0, curr_sum=0):
    if step == len(nums):
        res = reduce(lambda x, y: eval(f"{x}{y}"), operants)
        print("".join(operants), end='=')
        print(res)
        return

    for _ in range(2):
        curr_operant = i * '+' + j * '-'
        i, j = j, i
        operants.append(f"{curr_operant}{nums[step]}")
        expressions(nums, operants, 1, 0, step + 1, curr_sum+nums[step])
        operants.pop()
        curr_sum -= nums[step]


nums = [int(n) for n in input().split(', ')]
expressions(nums)
