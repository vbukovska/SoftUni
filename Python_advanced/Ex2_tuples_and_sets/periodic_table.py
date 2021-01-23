def input_lines_to_list(count):
    lines = []
    for _ in range(count):
        line = input().split()
        lines.extend(line)
    return lines


def custom_print(lines):
    for line in lines:
        print(line)


count_input_lines = int(input())

set_of_elements = set(input_lines_to_list(count_input_lines))
custom_print(set_of_elements)


