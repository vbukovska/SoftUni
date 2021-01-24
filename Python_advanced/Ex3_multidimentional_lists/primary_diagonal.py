def input_to_square_matrix(dim):
    matrix = []
    for row in range(dim):
        matrix.append([])
        input_column = [int(el) for el in input().split()]
        for column_el in input_column:
            matrix[row].append(column_el)
    return matrix


def sum_prime_diagonal(matrix):
    sum_diagonal = 0
    for row in range(len(matrix)):
        column = row
        sum_diagonal += matrix[row][column]
    return sum_diagonal


square_matrix_dimention = int(input())
square_matrix = input_to_square_matrix(square_matrix_dimention)


sum_matrix_diagonal = sum_prime_diagonal(square_matrix)
print(sum_matrix_diagonal)
