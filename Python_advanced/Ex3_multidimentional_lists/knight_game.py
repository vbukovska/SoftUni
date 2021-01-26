def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        # row = [int(n) for n in input().split()]
        row_string = input()
        row = []
        for ch in row_string:
            row.append(ch)
        matrix.append(row)
    return matrix


def count_all_moves(matrix):
    moves = []
    dim = len(matrix)
    for i in range(dim):
        moves.append([])
        for j in range(dim):
            moves[i].append(0)

    for r in range(dim):
        for c in range(dim):
            if matrix[r][c] == 'K':
                curr_moves = available_moves(dim, r, c)
                for move in curr_moves:
                    row_index = move[0]
                    column_index = move[1]
                    if matrix[row_index][column_index] == 'K':
                        moves[r][c] += 1
    return moves


def available_moves(dim, row, column):
    curr_moves = []
    search_knight_r = [-2, -2, -1, -1, 1, 1, 2, 2]
    search_knight_c = [-1, 1, -2, 2, -2, 2, -1, 1]
    for search_index in range(len(search_knight_c)):
        look_in_r = row + search_knight_r[search_index]
        look_in_c = column + search_knight_c[search_index]
        if look_in_r in range(dim) and look_in_c in range(dim):
            curr_moves.append((look_in_r, look_in_c))
    return curr_moves


def max_removal(dim, moves):
    max_removals = 0
    max_row = 0
    max_column = 0
    for r_move in range(dim):
        for c_move in range(dim):
            if max_removals < moves[r_move][c_move]:
                max_removals = moves[r_move][c_move]
                max_row = r_move
                max_column = c_move
    return max_removals, max_row, max_column


def knight_game_2(matrix, moves, number_moves):
    dim = len(moves)
    max_removals, r, c = max_removal(dim, moves)
    if max_removals > 0:
        curr_moves = available_moves(dim, r, c)
        moves[r][c] = 0
        matrix[r][c] = '0'
        number_moves += 1
        for move in curr_moves:
            move_rows = move[0]
            move_columns = move[1]
            if moves[move_rows][move_columns] > 0:
                moves[move_rows][move_columns] -= 1
        number_moves = knight_game_2(matrix, moves, number_moves)
    return number_moves


n = int(input())
matrix = input_to_matrix(n, n)
search_knight_r = [-2, -2, -1, -1, 1, 1, 2, 2]
search_knight_c = [-1, 1, -2, 2, -2, 2, -1, 1]

moves = count_all_moves(matrix)
num_removed_knights = knight_game_2(matrix, moves, 0)
print(num_removed_knights)

