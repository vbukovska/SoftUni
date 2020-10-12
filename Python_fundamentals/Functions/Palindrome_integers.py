numbers = input().split(', ')


def reverse_string(string):
    reversed_string = ''
    for char_index in range(-1, -len(string)-1, -1):
        reversed_string += string[char_index]
    return reversed_string


def is_palindrome(list_of_numbers):
    is_palindrome_number = [True] * len(list_of_numbers)
    for num in range(len(list_of_numbers)):
        half = len(list_of_numbers[num]) // 2
        first_half = list_of_numbers[num][:half]
        second_half = list_of_numbers[num][(len(list_of_numbers[num]) - half):]
        second_half = reverse_string(second_half)
        are_equal_half = True
        for digit in range(len(first_half)):
            if not first_half[digit] == second_half[digit]:
                are_equal_half = False
        is_palindrome_number[num] = are_equal_half
    return is_palindrome_number


result_list = is_palindrome(numbers)
for result in result_list:
    print(result)
