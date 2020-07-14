floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(rooms):
        if j == rooms - 1:
            if i == floors:
                print(f'L{i}{j}')
            elif i % 2 == 0:
                print(f'O{i}{j}')
            else:
                print(f'A{i}{j}')
        else:
            if i == floors:
                print(f'L{i}{j}', end=' ')
            elif i % 2 == 0:
                print(f'O{i}{j}', end=' ')
            else:
                print(f'A{i}{j}', end=' ')
