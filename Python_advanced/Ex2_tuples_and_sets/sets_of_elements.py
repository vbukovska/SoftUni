def input_lines_to_list(count):
    lines = []

    for _ in range(count):
        line = input()
        lines.append(line)

    return lines


def custom_print(lines):
    for line in lines:
        print(line)


first_input_count, second_input_count = map(int, input().split())

first_set = set(input_lines_to_list(first_input_count))
second_set = set(input_lines_to_list(second_input_count))

intersection_of_sets = first_set & second_set

custom_print(intersection_of_sets)