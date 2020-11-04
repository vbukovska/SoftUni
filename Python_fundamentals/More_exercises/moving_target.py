def in_range(index, target_list):
    return 0 <= index <= len(target_list) - 1


targets = [int(target) for target in input().split()]

while True:
    command_line = input()
    if command_line == 'End':
        print('|'.join([str(target) for target in targets]))
        break
    command, index, value = command_line.split()
    index = int(index)
    value = int(value)
    if command == 'Shoot':
        if in_range(index, targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif command == 'Add':
        if in_range(index, targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        left_index = index - value
        right_index = index + value
        if in_range(left_index, targets) and in_range(right_index, targets):
            targets = [targets[indx] for indx in range(len(targets)) if not left_index <= indx <= right_index]
        else:
            print('Strike missed!')
