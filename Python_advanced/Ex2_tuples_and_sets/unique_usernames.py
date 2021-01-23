def input_lines_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def custom_print(lines):
    for line in lines:
        print(line)


count_input_lines = int(input())

input_lines = input_lines_to_list(count_input_lines)

unique_users = set(input_lines)

custom_print(unique_users)