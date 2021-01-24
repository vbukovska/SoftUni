def input_to_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append([])
        input_column = [int(n) for n in input().split(', ')]
        for column in range(columns):
            matrix[row].append(input_column[column])
    return matrix


def sub_matrix(matrix, row, column):
    curr_sub_matrix = []
    for sub_row in range(2):
        curr_sub_matrix.append([])
        for sub_column in range(2):
            curr_sub_matrix[sub_row].append(matrix[row + sub_row][column + sub_column])
    return curr_sub_matrix


def sum_matrix_elements(matrix):
    result_sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            result_sum += matrix[row][column]
    return result_sum


def custom_print(matrix):
    for row in matrix:
        print(' '.join([str(el) for el in row]))


rows, columns = [int(n) for n in input().split(', ')]
matrix = input_to_matrix(rows, columns)

sum_sub_elements = []
sub_matrixes = []
for row in range(len(matrix) - 1):
    for column in range(len(matrix[row]) - 1):
        square_sub_matrix = sub_matrix(matrix, row, column)
        sub_matrixes.append(square_sub_matrix)
        sum_sub_elements.append(sum_matrix_elements(square_sub_matrix))

max_sum = 0
index_max_sum = 0
for index in range(len(sum_sub_elements)):
    if sum_sub_elements[index] > max_sum:
        max_sum = sum_sub_elements[index]
        index_max_sum = index

custom_print(sub_matrixes[index_max_sum])
print(max_sum)
