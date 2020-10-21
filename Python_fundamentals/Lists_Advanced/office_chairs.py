rooms = int(input())

free_chairs = 0
for room in range(rooms):
    curr_room = input().split()
    room_seats = [len(curr_room[index]) if index == 0 else -int(curr_room[index]) for index in range(len(curr_room))]
    curr_chairs_free = sum(room_seats)
    free_chairs += curr_chairs_free
    if curr_chairs_free < 0:
        print(f'{abs(curr_chairs_free)} more chairs needed in room {room + 1}')

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')

