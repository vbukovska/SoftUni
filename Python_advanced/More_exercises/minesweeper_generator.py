def mark_neighbour_mines(start_row, start_col, steps_to_neighbour):
    for step in steps_to_neighbour:
        row_step = step[0]
        col_step = step[1]
        curr_row = start_row + row_step
        curr_col = start_col + col_step
        if curr_row in range(dim) and curr_col in range(dim):
            if not field[curr_row][curr_col] == "*":
                field[curr_row][curr_col] += 1


def custom_print_matrix(matrix):
    for r in range(len(matrix)):
        print(' '.join(str(el) for el in matrix[r]))


dim = int(input())
number_bombs = int(input())
bombs = []
for _ in range(number_bombs):
    curr_bomb = input().split(", ")
    bomb_row = curr_bomb[0][1:]
    bomb_col = curr_bomb[1][:-1]
    bombs.append((bomb_row, bomb_col))

# create field with zeros
field = []
for row in range(dim):
    field.append([])
    for col in range(dim):
        field[row].append(0)

neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
# place bombs and count them in neighbour cells
for bomb in bombs:
    bomb_r = int(bomb[0])
    bomb_c = int(bomb[1])
    field[bomb_r][bomb_c] = "*"
    mark_neighbour_mines(bomb_r, bomb_c, neighbours)

custom_print_matrix(field)
