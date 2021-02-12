def input_to_matrix(rows):
    matrix = []
    for row_index in range(rows):
        row_string = input()
        row = []
        for ch in row_string:
            row.append(ch)
        matrix.append(row)
    return matrix


def find_the_position(matrix, search_for_symbol):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == search_for_symbol:
                return r, c


def make_a_move(field_dim, position, command):
    curr_row = position[0]
    curr_col = position[1]
    if command == 'up':
        new_row = curr_row - 1
        new_col = curr_col
    elif command == 'down':
        new_row = curr_row + 1
        new_col = curr_col
    elif command == 'left':
        new_row = curr_row
        new_col = curr_col - 1
    else:
        new_row = curr_row
        new_col = curr_col + 1

    if new_row in range(field_dim) and new_col in range(field_dim):
        return new_row, new_col
    return curr_row, curr_col


def swap_possitions(matrix, snake_possition, new_possition):
    snake_r, snake_c = snake_possition
    r, c = new_possition
    territory[r][c] = "S"
    territory[snake_r][snake_c] = "."
    return r, c


def custom_print_matrix(matrix):
    for r in range(len(matrix)):
        print(''.join(str(el) for el in matrix[r]))


REQUIRED_FOOD = 10
territory_dim = int(input())
food_quantity = 0

territory = input_to_matrix(territory_dim)

snake_possition = find_the_position(territory, "S")
snake_row = snake_possition[0]
snake_col = snake_possition[1]

while True:
    command = input()
    row, col = make_a_move(territory_dim, (snake_row, snake_col), command)
    if snake_row == row and snake_col == col:
        territory[snake_row][snake_col] = "."
        print("Game over!")
        break
    if territory[row][col] == "*":
        food_quantity += 1
        snake_row, snake_col = swap_possitions(territory, (snake_row, snake_col), (row, col))
        if food_quantity == REQUIRED_FOOD:
            print("You won! You fed the snake.")
            break
    elif territory[row][col] == "B":
        snake_row, snake_col = swap_possitions(territory, (snake_row, snake_col), (row, col))
        row, col = find_the_position(territory, "B")
        snake_row, snake_col = swap_possitions(territory, (snake_row, snake_col), (row, col))
    else:
        snake_row, snake_col = swap_possitions(territory, (snake_row, snake_col), (row, col))

print(f"Food eaten: {food_quantity}")
custom_print_matrix(territory)

