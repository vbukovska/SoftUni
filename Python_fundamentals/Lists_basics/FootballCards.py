# cards = input().split(' ')
# team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# removed_A = []
# team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# removed_B = []
#
# for i in range(len(cards)):
#     if 'A' in cards[i] and not cards[i][2:] in removed_A:
#         removed_A.append(cards[i][2:])
#         team_A.remove(int(cards[i][2:]))
#         if len(team_A) < 7:
#             break
#     if 'B' in cards[i] and not cards[i][2:] in removed_B:
#         removed_B.append(cards[i][2:])
#         team_B.pop(int(cards[i][2:]))
#         if len(team_B) < 7:
#             break
#
# print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
# if len(team_A) < 7 or len(team_B) < 7:
#     print('Game was terminated')
# Judge gives runtime error

cards = input().split(' ')
team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
removed_A = []
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
removed_B = []
team = []
player = []

for i in range(len(cards)):
    team.append(cards[i][0])
    player.append(cards[i][2:])

for curr_card in range(len(team)):
    if team[curr_card] == 'A' and not player[curr_card] in removed_A:
        removed_A.append(player[curr_card])
        team_A.remove(int(player[curr_card]))
        if len(team_A) < 7:
            break
    if team[curr_card] == 'B' and not player[curr_card] in removed_B:
        removed_B.append(player[curr_card])
        team_B.remove(int(player[curr_card]))
        if len(team_B) < 7:
            break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
if len(team_A) < 7 or len(team_B) < 7:
    print('Game was terminated')
