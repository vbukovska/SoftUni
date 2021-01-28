def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        row = [int(n) for n in input().split()]
        # row = input().split()
        matrix.append(row)
    return matrix


def curr_position_targets(matrix, row, column, pattern_r, pattern_c):
    curr_targets = []
    dim = len(matrix)
    for index in range(len(pattern_c)):
        look_in_r = row + pattern_r[index]
        look_in_c = column + pattern_c[index]
        if look_in_r in range(dim) and look_in_c in range(dim):
            curr_targets.append((look_in_r, look_in_c))
    return curr_targets


def bombs_game(matrix, bombs, pattern_r, pattern_c):
    dim = len(matrix)
    for bomb in bombs:
        bomb_row = bomb[0]
        bomb_column = bomb[1]
        if matrix[bomb_row][bomb_column] > 0:
            curr_targets = curr_position_targets(matrix, bomb_row, bomb_column, pattern_r, pattern_c)
            for target in curr_targets:
                target_row = target[0]
                target_column = target[1]
                if matrix[target_row][target_column] > 0:
                    matrix[target_row][target_column] -= matrix[bomb_row][bomb_column]
            matrix[bomb_row][bomb_column] = 0
    return matrix


def count_positive_elements(matrix):
    counter = 0
    tot_sum = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] > 0:
                counter += 1
                tot_sum += matrix[r][c]
    return counter, tot_sum


def custom_print(matrix):
    alice_cells, result_sum = count_positive_elements(matrix)
    print(f'Alive cells: {alice_cells}')
    print(f'Sum: {result_sum}')
    for r in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[r]))



n = int(input())
matrix = input_to_matrix(n, n)
bombs = input().split()

for index in range(len(bombs)):
    bombs[index] = [int(c) for c in bombs[index].split(',')]

pattern_r = [-1, -1, -1, 0, 0, 1, 1, 1]
pattern_c = [-1, 0, 1, -1, 1, -1, 0, 1]

result_matrix = bombs_game(matrix, bombs, pattern_r, pattern_c)
custom_print(result_matrix)