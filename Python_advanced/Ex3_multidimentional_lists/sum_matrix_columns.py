def input_to_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append([])
        input_row = [int(el) for el in input().split()]
        for column_el in range(columns):
            matrix[row].append(input_row[column_el])
    return matrix


def list_of_matrix_columns_sum(matrix):
    columns_sum = []
    number_matrix_columns = len(matrix[0])
    for column in range(number_matrix_columns):
        column_sum = 0
        for row in matrix:
            column_sum += row[column]
        columns_sum.append(column_sum)
    return columns_sum


def custom_print(lines):
    [print(line) for line in lines]


number_rows, number_columns = [int(n) for n in input().split(', ')]
matrix = input_to_matrix(number_rows, number_columns)

columns_sum = list_of_matrix_columns_sum(matrix)
custom_print(columns_sum)