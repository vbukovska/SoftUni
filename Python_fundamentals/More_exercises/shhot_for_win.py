def in_range(index, target_list):
    return 0 <= index <= len(target_list) - 1


def reduce(target, value):
    if target == -1:
        return -1
    else:
        return target - value


def increase(target, value):
    if target == -1:
        return -1
    else:
        return target + value


targets = [int(target) for target in input().split()]

while True:
    command = input()
    if command == 'End':
        shot_targets = len([target for target in targets if target == -1])
        print(f"Shot targets: {shot_targets} -> {' '.join([str(target) for target in targets])}")
        break
    index = int(command)
    if in_range(index, targets) and not targets[index] == -1:
        target_value = targets[index]
        targets = [reduce(target, target_value) if target > target_value else increase(target, target_value) for target in targets]
        targets[index] = -1
