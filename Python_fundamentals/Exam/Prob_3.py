people_info = {}

while True:
    command_line = input().split(':')
    command = command_line[0]
    if command == 'Results':
        break
    if command == 'Add':
        name = command_line[1]
        health = int(command_line[2])
        energy = int(command_line[3])
        if name not in people_info:
            people_info[name] = {'health': 0, 'energy': energy}
        people_info[name]['health'] += health
        # people_info[name]['energy'] += energy
    elif command == 'Attack':
        attacker_name = command_line[1]
        defender_name = command_line[2]
        damage = int(command_line[3])
        if attacker_name in people_info and defender_name in people_info:
            people_info[defender_name]['health'] -= damage
            if people_info[defender_name]['health'] <= 0:
                people_info.pop(defender_name)
                print(f"{defender_name} was disqualified!")
            people_info[attacker_name]['energy'] -= 1
            if people_info[attacker_name]['energy'] == 0:
                people_info.pop(attacker_name)
                print(f"{attacker_name} was disqualified!")
    elif command == 'Delete':
        username = command_line[1]
        if username == 'All':
            people_info.clear()
        elif username in people_info:
            people_info.pop(username)

print(f"People count: {len(people_info)}")


people_info = dict(sorted(people_info.items(), key=lambda x: (-x[1]['health'], x[0])))

for person in people_info:
    print(f"{person} - {people_info[person]['health']} - {people_info[person]['energy']}")