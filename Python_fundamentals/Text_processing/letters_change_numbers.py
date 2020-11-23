strings = input().split()

total_result = 0

for string in strings:
    prefix_letter = string[0]
    prefix_ascii_code = ord(prefix_letter)

    suffix_letter = string[-1]
    suffix_ascii_code = ord(suffix_letter)

    number = int(string[1:-1])

    if prefix_letter.isupper():
        alphabet_position = prefix_ascii_code - 64
        total_result += number / alphabet_position
    else:
        alphabet_position = prefix_ascii_code - 96
        total_result += number * alphabet_position

    if suffix_letter.isupper():
        alphabet_position = suffix_ascii_code - 64
        total_result -= alphabet_position
    else:
        alphabet_position = suffix_ascii_code - 96
        total_result += alphabet_position

print(f"{round(total_result, 2):.2f}")
