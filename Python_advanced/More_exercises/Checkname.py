def input_to_matrix(rows):
    matrix = []
    for row_index in range(rows):
        # row = [int(n) for n in input().split()]
        row = input().split()
        matrix.append(row)
    return matrix


def find_the_king(matrix):
    start_symbol = 'K'
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == start_symbol:
                return r, c


def find_possible_attacks(start_row, start_col, row_step, col_step):
    curr_row = start_row + row_step
    curr_col = start_col + col_step
    while curr_row in range(dim) and curr_col in range(dim):
        if field[curr_row][curr_col] == "Q":
            return [curr_row, curr_col]
        curr_row += row_step
        curr_col += col_step


dim = 8

field = input_to_matrix(dim)
king = find_the_king(field)
king_row = king[0]
king_column = king[1]
queens = []

# search queens
possible_directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
for direction in possible_directions:
    row_step = direction[0]
    col_step = direction[1]
    queen = find_possible_attacks(king_row, king_column, row_step, col_step)
    if queen:
        queens. append(queen)


if queens:
    [print(queen) for queen in queens]
else:
    print("The king is safe!")
