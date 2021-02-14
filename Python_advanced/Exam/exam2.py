from math import floor


def input_to_matrix(rows):
    matrix = []
    for row_index in range(rows):
        row = input().split()
        matrix.append(row)
    return matrix


def find_the_player(matrix):
    start_symbol = 'P'
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == start_symbol:
                return r, c


def make_a_move(field_dim, curr_row, curr_col, command):
    if command == 'up':
        new_row = curr_row - 1
        new_col = curr_col
    elif command == 'down':
        new_row = curr_row + 1
        new_col = curr_col
    elif command == 'left':
        new_row = curr_row
        new_col = curr_col - 1
    elif command == 'right':
        new_row = curr_row
        new_col = curr_col + 1

    if new_row in range(field_dim) and new_col in range(field_dim):
        return new_row, new_col
    return curr_row, curr_col


dim = int(input())

field = input_to_matrix(dim)
player_possition = find_the_player(field)
player_row = player_possition[0]
player_col = player_possition[1]
is_win = False
collected_coins = 0
player_path = []

while True:
    command = input()
    if command not in ("up", "down", "left", "right"):
        continue
    curr_position = make_a_move(dim, player_row, player_col, command)
    curr_row = curr_position[0]
    curr_col = curr_position[1]
    if player_possition == curr_position:
        break
    elif field[curr_row][curr_col] == "X":
        break
    else:
        collected_coins += int(field[curr_row][curr_col])
        player_path.append(curr_position)
        field[curr_row][curr_col] = '0'
        player_possition = curr_position
        player_row = curr_row
        player_col = curr_col
        if collected_coins >= 100:
            is_win = True
            break

if is_win:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {floor(collected_coins/2)} coins.")

print("Your path:")
for coordinate in player_path:
    print(f"[{coordinate[0]}, {coordinate[1]}]")