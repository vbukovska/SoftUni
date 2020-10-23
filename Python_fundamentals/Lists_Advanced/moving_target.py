targets_power = [int(power) for power in input().split()]

while True:
    # command_line = [int(el) if el.isnumeric() else el for el in input().split()]
    command_line = input().split()
    command = command_line[0]

    if command == 'End':
        print('|'.join([str(num) for num in targets_power]))
        break

    index = int(command_line[1])
    power = int(command_line[2])

    if command == 'Shoot' and 0 <= index < len(targets_power):
        if targets_power[index] - power <= 0:
            targets_power.pop(index)
        else:
            targets_power[index] -= power
    elif command == 'Add':
        if 0 <= index < len(targets_power):
            targets_power.insert(index, power)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        upper_range = index + power
        lower_range = index - power
        if lower_range >= 0 and upper_range < len(targets_power):
            targets_power = targets_power[:lower_range] + targets_power[upper_range + 1:]
        else:
            print('Strike missed!')

