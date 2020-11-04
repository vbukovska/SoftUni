health = 100
bitcoins = 0

dungeons_rooms = input().split('|')
for room in range(len(dungeons_rooms)):
    command, number = dungeons_rooms[room].split()
    value = int(number)
    if command == 'potion':
        if health + value > 100:
            healed = 100 - health
            health = 100
        else:
            healed = value
            health += healed
        print(f'You healed for {healed} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += value
        print(f'You found {value} bitcoins.')
    else:
        health -= value
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room + 1}')
            break

if health > 0:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')

