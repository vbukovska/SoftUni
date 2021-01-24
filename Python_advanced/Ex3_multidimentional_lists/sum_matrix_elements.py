# def input_to_matrinx(rows, columns):
#     matrix = []
#     for row in range(rows):
#         input_row = [int(el) for el in input().split(', ')]
#         matrix.append(input_row)
#     return matrix


def input_to_matrinx(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append([])
        input_row = [int(el) for el in input().split(', ')]
        for column in range(columns):
            matrix[row].append(input_row[column])
    return matrix


def sum_matrix_elements(matrix):
    sum_elements = 0
    for row in matrix:
        for column in row:
            sum_elements += column
    return sum_elements


number_rows, number_columns = [int(n) for n in input().split(', ')]

matrix = input_to_matrinx(number_rows, number_columns)

sum_elements = sum_matrix_elements(matrix)
print(sum_elements)
print(matrix)
