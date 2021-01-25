# reads a rectangular integer matrix of size N x M and find the square 3 x 3 that has maximal sum of its elements.
def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        row = [int(n) for n in input().split()]
        matrix.append(row)
    return matrix


def sum_square_matrixes(matrix, row, column, dim):
    sum_elements = 0
    sub_matrix = []
    for r in range(row, row + dim):
        for c in range(column, column + dim):
            sum_elements += matrix[r][c]
        sub_matrix.append(matrix[r][column:column + dim])
    return sum_elements, sub_matrix


def custom_print_matrix(matrix):
    for r in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[r]))


rows_count, columns_count = [int(n) for n in input().split()]
matrix = input_to_matrix(rows_count, columns_count)
sub_matrix_dim = 3
best_sum, best_matrix = sum_square_matrixes(matrix, 0, 0, sub_matrix_dim)

for row_index in range(rows_count - sub_matrix_dim + 1):
    for col_index in range(columns_count - sub_matrix_dim + 1):
        curr_sum, curr_matrix = sum_square_matrixes(matrix, row_index, col_index, sub_matrix_dim)
        if best_sum < curr_sum:
            best_sum = curr_sum
            best_matrix = curr_matrix

print(f'Sum = {best_sum}')
custom_print_matrix(best_matrix)

