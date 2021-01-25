def input_to_matrix(rows, columns):
    matrix = []
    for row_index in range(rows):
        # row = [int(n) for n in input().split()]
        row = input().split()
        matrix.append(row)
    return matrix


def is_valid_command(command, coordinates, matrix_rows, matrix_columns):
    if not command == 'swap':
        return False
    if not len(coordinates) == 4:
        return False
    for index in range(len(coordinates)):
        if index % 2 == 0:
            if not coordinates[index] in range(matrix_rows):
                return False
        elif not coordinates[index] in range(matrix_columns):
            return False
    return True


def swap_coordinates(matrix, coordinates):
    row_1, col_1, row_2, col_2 = coordinates
    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
    return matrix


def custom_print_matrix(matrix):
    for r in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[r]))


rows_count, columns_count = [int(n) for n in input().split()]
matrix = input_to_matrix(rows_count, columns_count)
while True:
    command, *coordinates = input().split()
    if command == 'END':
        break
    coordinates = [int(n) if n.isdigit() else n for n in coordinates]
    if not is_valid_command(command, coordinates, rows_count, columns_count):
        print('Invalid input!')
    else:
        matrix = swap_coordinates(matrix, coordinates)
        custom_print_matrix(matrix)

