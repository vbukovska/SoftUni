# recusrion
# def best_list_pureness(numbers, rotation, i=0):
#     if rotation == 0:
#         max_pureness = sum([i * numbers[i] for i in range(len(numbers))])
#         max_rotation = rotation
#         if i == 0:
#             return f"Best pureness {max_pureness} after {max_rotation} rotations"
#         return numbers, (max_pureness, rotation)
#     numbers, max_result = best_list_pureness(numbers, rotation - 1, i + 1)
#     max_pureness = max_result[0]
#     max_rotation = max_result[1]
#     last = numbers.pop()
#     numbers.insert(0, last)
#     curr_pureness = sum([i * numbers[i] for i in range(len(numbers))])
#     if curr_pureness > max_pureness:
#         max_pureness = curr_pureness
#         max_rotation = rotation
#     if i > 0:
#         return numbers, (max_pureness, max_rotation)
#     return f"Best pureness {max_pureness} after {max_rotation} rotations"


def best_list_pureness(*args):
    numbers = args[0]
    rotations = args[1]
    pureness = []
    pureness_sum = sum([i * numbers[i] for i in range(len(numbers))])
    pureness.append((pureness_sum, 0))
    max_pureness = pureness_sum
    max_rotation = 0
    for rotation in range(1, rotations + 1):
        last = numbers.pop()
        numbers.insert(0, last)
        pureness_sum = sum([i * numbers[i] for i in range(len(numbers))])
        pureness.append((pureness_sum, rotation))

    for index in range(len(pureness)):
        curr_pureness = pureness[index][0]
        curr_rotation = pureness[index][1]
        if index == 0:
            max_pureness = curr_pureness
            max_rotation = curr_rotation

        if curr_pureness > max_pureness:
            max_pureness = curr_pureness
            max_rotation = curr_rotation

    return f"Best pureness {max_pureness} after {max_rotation} rotations"



test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
test = ([5, 1, 2, 3, 4], 4)
result = best_list_pureness(*test)
print(result)

test = ([1, 1, 1, 1, 1], 10)
result = best_list_pureness(*test)
print(result)
test = ([1, 1, 1, 1, 1], 0)
result = best_list_pureness(*test)
print(result)
