def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def custom_print(result):
    print(', '.join(map(str, result)))


number_lines = int(input())
names = input_to_list(number_lines)
odd_numbers = set()
even_numbers = set()

for index in range(len(names)):
    name = names[index]
    sum_ascii = sum([ord(char) for char in name])
    curr_line = index + 1
    division_result = sum_ascii // curr_line
    if division_result % 2 == 0:
        even_numbers.add(division_result)
    else:
        odd_numbers.add(division_result)

sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odd == sum_even:
    result_set = even_numbers.union(odd_numbers)
elif sum_odd > sum_even:
    result_set = odd_numbers.difference(even_numbers)
else:
    result_set = odd_numbers.symmetric_difference(even_numbers)

custom_print(result_set)
