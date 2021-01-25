# calculates the absolute difference of main and secondary matrix diagonal
def input_to_square_matrix(dim):
    matrix = []
    for row_index in range(dim):
        input_row = [int(el) for el in input().split()]
        matrix.append(input_row)
    return matrix


def prime_diagonal_sum(matrix):
    dim = len(matrix)
    sum_diagonal = 0
    for index in range(dim):
        sum_diagonal += matrix[index][index]
    return sum_diagonal


def secondary_diagonal_sum(matrix):
    dim = len(matrix)
    sum_diagonal = 0
    for row_index in range(dim):
        column_index = dim - row_index - 1
        sum_diagonal += matrix[row_index][column_index]
    return sum_diagonal


dim_matrix = int(input())
matrix = input_to_square_matrix(dim_matrix)
sum_prime_diagonal = prime_diagonal_sum(matrix)
sum_secondary_diagonal = secondary_diagonal_sum(matrix)
difference_sum_diagonals = abs(sum_prime_diagonal - sum_secondary_diagonal)
print(difference_sum_diagonals)
