from _collections import deque

water_quantity = int(input())

water_que = deque()

while True:
    name = input()
    if name == 'Start':
        break
    water_que.append(name)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if 'refill' in command:
        liters = int(command[1])
        water_quantity += liters
    else:
        liters = int(command[0])
        person_name = water_que.popleft()
        if water_quantity >= liters:
            water_quantity -= liters
            print(f'{person_name} got water')
        else:
            print(f'{person_name} must wait')

print(f'{water_quantity} liters left')