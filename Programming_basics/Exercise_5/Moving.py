width = int(input())
length = int(input())
height = int(input())

room_space = width * length * height
tot_packages = 0

while tot_packages <= room_space:
    command = input()
    if command == 'Done':
        print(f'{room_space - tot_packages} Cubic meters left.')
        break

    tot_packages += int(command)

if command != 'Done':
    print(f'No more free space! You need {tot_packages - room_space} Cubic meters more.')

