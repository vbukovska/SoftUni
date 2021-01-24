def input_to_square_matrix(dim):
    matrix = []
    for row in range(dim):
        matrix.append([])
        input_column = input()
        for column_el in input_column:
            matrix[row].append(column_el)
    return matrix


def first_occurrence(symbol, matrix):
    matrix_dim = len(matrix)
    for row_index in range(matrix_dim):
        for column_index in range(matrix_dim):
            if matrix[row_index][column_index] == symbol:
                return row_index, column_index


def custom_print(result):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


square_matrix_dim = int(input())
character_matrix = input_to_square_matrix(square_matrix_dim)
symbol = input()

result = first_occurrence(symbol, character_matrix)
custom_print(result)




