def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        # row = [int(n) for n in input().split()]
        row = input().split()
        matrix.append(row)
    return matrix


def find_starting_point(matrix):
    start_symbol = 's'
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == start_symbol:
                return r, c


def count_elements_in_matrix(matrix, el):
    counter = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == el:
                counter += 1
    return counter


def make_a_move(field_dim, position, command):
    curr_row = position[0]
    curr_col = position[1]
    if command == 'up':
        new_row = curr_row - 1
        new_col = curr_col
    elif command == 'down':
        new_row = curr_row + 1
        new_col = curr_col
    elif command == 'left':
        new_row = curr_row
        new_col = curr_col - 1
    else:
        new_row = curr_row
        new_col = curr_col + 1

    if new_row in range(field_dim) and new_col in range(field_dim):
        return new_row, new_col
    return curr_row, curr_col


def miner_game(matrix, commands):
    dim = len(matrix)
    collected_coals = 0
    result = 'not_finished'
    field_coals = count_elements_in_matrix(matrix, 'c')
    remain_coals = field_coals
    starting_position = find_starting_point(matrix)
    current_position = starting_position
    for command in commands:
        current_position = make_a_move(dim, current_position, command)
        if matrix[current_position[0]][current_position[1]] == 'e':
            result = 'end'
            break
        elif matrix[current_position[0]][current_position[1]] == 'c':
            matrix[current_position[0]][current_position[1]] = '*'
            collected_coals += 1
            remain_coals -= 1
            if remain_coals == 0:
                result = 'win'
                break
    return result, current_position, collected_coals, remain_coals


def custom_print_game_results(result, position, points, remaining):
    position_row = position[0]
    position_col = position[1]
    if result == 'end':
        print(f'Game over! ({position_row}, {position_col})')
    elif result == 'win':
        print(f'You collected all coals! ({position_row}, {position_col})')
    else:
        print(f'{remaining} coals left. ({position_row}, {position_col})')


n = int(input())
commands = input().split()
field = input_to_matrix(n, n)
result, position, coals_collected, remain_coals = miner_game(field, commands)
custom_print_game_results(result, position, coals_collected, remain_coals)
