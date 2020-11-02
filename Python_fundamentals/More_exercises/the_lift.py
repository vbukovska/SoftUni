people_in_queue = int(input())
lift = [int(people_in_wagon) for people_in_wagon in input().split()]
curr_wagon = 0
for wagon in range(curr_wagon, len(lift)):
    if people_in_queue == 0:
        break
    else:
        wagon_free_place = 4 - lift[wagon]
        if wagon_free_place > 0:
            if people_in_queue >= wagon_free_place:
                lift[wagon] = 4
                people_in_queue -= wagon_free_place
            else:
                lift[wagon] += people_in_queue
                people_in_queue = 0

is_wagon_full = sum(lift) >= len(lift) * 4
if people_in_queue <= 0:
    if not is_wagon_full:
        print("The lift has empty spots!")
elif people_in_queue > 0:
    print(f"There isn't enough space! {people_in_queue} people in a queue!")
print(' '.join(list(map(str, lift))))

