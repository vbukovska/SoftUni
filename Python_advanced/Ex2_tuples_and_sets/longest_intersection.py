def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append([x.split(',') for x in input().split('-')])
    return lines


def get_ranges(pairs):
    first_range_limits, second_range_limits = pairs
    first = set(range(int(first_range_limits[0]), int(first_range_limits[1]) + 1))
    second = set(range(int(second_range_limits[0]), int(second_range_limits[1]) + 1))
    return first, second


def custom_print(range):
    string_range = ', '.join(map(str, range))
    range_len = len(range)
    print(f'Longest intersection is [{string_range}] with length {range_len}')


count_input_lines = int(input())
ranges = input_to_list(count_input_lines)

max_intersection = set()

for ranges_pairs in ranges:
    first_range, second_range = get_ranges(ranges_pairs)
    intersection_range = first_range & second_range
    if len(max_intersection) < len(intersection_range):
        max_intersection = intersection_range

custom_print(max_intersection)
