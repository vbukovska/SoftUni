ttt_list = []
player_1 = '1'
player_2 = '2'
points = 1
row = 0
column = 0
winner = ''
for line in range(3):
    ttt_list.append(input().split())

for row in range(3):
    for col in range(3):
        winner = ttt_list[row][col]
        if ttt_list[row][col] == '0':
            break
        elif col == 0:
            continue
        elif not ttt_list[row][col] == ttt_list[row][col - 1]:
            break
        else:
            points += 1
    if points == 3:
        break
if points == 3:
    if winner == '1':
        quit(print('First player won'))
    else:
        quit(print('Second player won'))
# print

for col in range(3):
    for row in range(3):
        winner = ttt_list[row][col]
        if ttt_list[row][col] == '0':
            break
        elif row == 0:
            continue
        elif not ttt_list[row][col] == ttt_list[row - 1][col]:
            break
        else:
            points += 1
    if points == 3:
        break
if points == 3:
    if winner == '1':
        quit(print('First player won'))
    else:
        quit(print('Second player won'))


if ttt_list[0][0] == ttt_list[1][1] == ttt_list[2][2]:
    if ttt_list[0][0] == '1':
        quit(print('First player won'))
    elif ttt_list[0][0] == '2':
        quit(print('Second player won'))
elif ttt_list[0][2] == ttt_list[1][1] == ttt_list[2][0]:
    if ttt_list[0][2] == '1':
        quit(print('First player won'))
    elif ttt_list[0][2] == '2':
        quit(print('First player won'))
else:
    print('Draw!')



# if player_1 > player_2:
#     print('First player won')
# elif player_2 > player_1:
#     print('Second player won')
# else:
#     print('Draw!')
