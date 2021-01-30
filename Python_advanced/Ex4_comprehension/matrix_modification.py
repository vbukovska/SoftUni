def input_to_matrix(rows):
    matrix = []
    for row_index in range(rows):
        row = [int(n) for n in input().split()]
        # row = input().split()
        matrix.append(row)
    return matrix


dim = int(input())
matrix = input_to_matrix(dim)

while True:
    command, *coordinates = input().split()
    if command == 'END':
        break
    row = int(coordinates[0])
    col = int(coordinates[1])
    value = int(coordinates[2])
    if not (row in range(dim) and col in range(dim)):
        print('Invalid coordinates')
        continue
    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

[print(' '.join([str(el) for el in row])) for row in matrix]