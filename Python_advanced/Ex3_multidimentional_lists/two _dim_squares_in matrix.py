# finds the equal character 2X2 square sub-matrixes in a matrix
def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


def is_square_sub_matrix(matrix, row, column, sub_dim):
    char = matrix[row][column]
    for r in range(row, row + sub_dim):
        for c in range(column, column + sub_dim):
            if not matrix[r][c] == char:
                return False
    return True



rows, columns = [int(n) for n in input().split()]
matrix = input_to_matrix(rows, columns)

sub_matrix_dimention = 2
number_square_matrixes = 0

for row_index in range(rows - sub_matrix_dimention + 1):
    for column_index in range(columns - sub_matrix_dimention + 1):
        is_sub_matrix = is_square_sub_matrix(matrix, row_index, column_index, sub_matrix_dimention)
        if is_sub_matrix:
            number_square_matrixes += 1
print(number_square_matrixes)

