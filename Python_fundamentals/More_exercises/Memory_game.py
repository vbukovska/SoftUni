def in_range(index, sequence):
    return 0 <= index <= len(sequence) - 1


elements = input().split()
curr_moves = 0
cmd = input()

while elements:
    if cmd == 'end' or len(elements) == 0:
        break
    curr_moves += 1
    first_el, second_el = list(map(int, cmd.split()))
    if first_el == second_el or not in_range(first_el, elements) or not in_range(second_el, elements):
        print('Invalid input! Adding additional elements to the board')
        middle_index = int(len(elements) / 2)
        new_element = f'-{curr_moves}a'
        sub_list = [new_element, new_element]
        elements[middle_index:middle_index] = sub_list
    elif elements[first_el] == elements[second_el]:
        matched_element = elements[first_el]
        print(f'Congrats! You have found matching elements - {matched_element}!')
        elements = [el for el in elements if not el == matched_element]
    else:
        print('Try again!')
    cmd = input()

if cmd == 'end':
    print(f'Sorry you lose :(')
    print(' '.join(list(map(str, elements))))
else:
    print(f'You have won in {curr_moves} turns!')
