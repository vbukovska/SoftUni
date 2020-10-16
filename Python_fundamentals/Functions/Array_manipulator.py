def exchange(list_of_elements, slice_index):
    if slice_index >= len(list_of_elements) or slice_index < 0:
        print('Invalid index')
        return list_of_elements
    first_part = list_of_elements[:slice_index+1]
    second_part = list_of_elements[slice_index+1:]
    result_list = second_part + first_part
    return result_list


def even_or_odd(list_of_elements, type_of_number):
    if type_of_number == 'even':
        return [n for n in list_of_elements if n % 2 == 0]
    else:
        return [n for n in list_of_elements if not n % 2 == 0]


def min_max(list_of_elements, command):
    if command == 'max':
        return max(list_of_elements)
    else:
        return min(list_of_elements)


def last_index(list_of_elements, element):
    for el in range(len(list_of_elements)-1, -1, -1):
        if list_of_elements[el] == element:
            return el


# def get_reverse(list_of_elements, command):
#     if command == 'first':
#         return list_of_elements
#     else:
#         return list_of_elements[::-1]


def first_last_n(list_of_elements, command, count):
    if command == 'first':
        return list_of_elements[:count]
    else:
        return list_of_elements[len(list_of_elements)-count:]


string_list = input().split(' ')
list_of_numbers = [int(x) for x in string_list]
while True:
    command = input().split()
    if command[0] == 'end':
        print(list_of_numbers)
        break
    elif command[0] == 'exchange':
        list_of_numbers = exchange(list_of_numbers, int(command[1]))
    elif command[0] in ['max', 'min']:
        target_numbers = even_or_odd(list_of_numbers, command[1])
        if len(target_numbers) == 0:
            print('No matches')
        else:
            element = min_max(target_numbers, command[0])
            result = last_index(list_of_numbers, element)
            print(result)
    elif command[0] in ['first', 'last']:
        if int(command[1]) > len(list_of_numbers):
            print('Invalid count')
        else:
            # target_numbers = get_reverse(list_of_numbers, command[0])
            # result = even_or_odd(target_numbers, command[2])[:int(command[1])]
            # print(result[::-1])
            target_numbers = even_or_odd(list_of_numbers, command[2])
            result = first_last_n(target_numbers, command[0], int(command[1]))
            print(result)
