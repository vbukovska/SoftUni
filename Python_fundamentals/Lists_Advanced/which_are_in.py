# from more_itertools import unique_everseen
# library more_intertools need to be installed


def unique_elements(input_list):
    unique_result = []
    for word in input_list:
        if word not in unique_result:
            unique_result.append(word)
    return unique_result


string_1 = input().split(', ')
string_2 = input().split(', ')
result = [word_1 for word_1 in string_1 for word_2 in string_2 if word_1 in word_2]

print(unique_elements(result))

