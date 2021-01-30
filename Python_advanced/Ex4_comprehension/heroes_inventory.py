names = input().split(', ')
players = {name: {} for name in names}
while True:
    command = input()
    if command == 'End':
        break
    name, item, cost = command.split('-')
    player = {name: {'Items': item, 'Cost': int(cost)}}
    if item not in players[name]:
        players[name][item] = int(cost)

result = {key: [len(players[key]), sum(players[key].values())] if players[key].values() else [0, 0] for key in players}

[print(f'{key} -> Items: {result[key][0]}, Cost: {result[key][1]}') for key in result]