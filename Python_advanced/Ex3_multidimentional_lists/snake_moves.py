def create_snake_matrix(rows, columns, snake):
    matrix = []
    el = 0
    for i in range(rows):
        matrix.append([])
        if i % 2 == 0:
            for j in range(columns):
                matrix[i].append(snake[el])
                if el < len(snake) - 1:
                    el += 1
                else:
                    el = 0

        else:
            for j in range(-1, -columns - 1, -1):
                matrix[i].insert(j, snake[el])
                if el < len(snake) - 1:
                    el += 1
                else:
                    el = 0
    return matrix


def custom_print(matrix):
    for r in range(len(matrix)):
        print(''.join(matrix[r]))


# SoftUni
rows, columns = [int(n) for n in input().split()]
snake = input()
snake_matrix = create_snake_matrix(rows, columns, snake)
custom_print(snake_matrix)


