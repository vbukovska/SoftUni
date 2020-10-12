password = input()


def are_enough_characters(string):
    if not len(string) in range(6, 11):
        return False
    else:
        return True


def are_valid_characters(string):
    digits = range(48, 58)
    capital_letters = range(65, 91)
    small_letters = range(97, 123)
    is_valid_character = True
    for character in string:
        ascii_character = ord(character)
        if ascii_character not in digits and ascii_character not in capital_letters and ascii_character not in small_letters:
            is_valid_character = False
    return is_valid_character


def are_enough_digits(string):
    count_digits = 0
    for character in string:
        ascii_character = ord(character)
        if ascii_character in range(48, 58):
            count_digits += 1
    if count_digits >= 2:
        return True
    else:
        return False


def is_valid_password(string):
    result = []
    is_first_check = are_enough_characters(string)
    is_second_check = are_valid_characters(string)
    is_third_check = are_enough_digits(string)
    result.append(is_first_check)
    result.append(is_second_check)
    result.append(is_third_check)
    return result


checks_result = is_valid_password(password)
if checks_result[0] & checks_result[1] & checks_result[2]:
    print('Password is valid')
else:
    if not checks_result[0]:
        print('Password must be between 6 and 10 characters')
    if not checks_result[1]:
        print('Password must consist only of letters and digits')
    if not checks_result[2]:
        print('Password must have at least 2 digits')