number = int(input())

plants_rarity = {}
plants_rating = {}

for _ in range(number):
    plant, rarity = input().split('<->')
    plants_rarity[plant] = int(rarity)

while True:
    command_line = input()
    if command_line == 'Exhibition':
        break
    command, parameters = command_line.split(': ')
    if command == 'Rate':
        curr_plant, rating = parameters.split(' - ')
        rating = int(rating)
        if curr_plant not in plants_rarity:
            print('error')
        else:
            if curr_plant not in plants_rating:
                plants_rating[curr_plant] = []
            plants_rating[curr_plant].append(rating)
    elif command == 'Update':
        curr_plant, new_rarity = parameters.split(' - ')
        new_rarity = int(new_rarity)
        if curr_plant in plants_rarity:
            plants_rarity[curr_plant] = new_rarity
        else:
            print('error')
    elif command == 'Reset':
        curr_plant = parameters
        if curr_plant in plants_rating:
            plants_rating.pop(curr_plant)
        else:
            print('error')
    else:
        print('error')

plants_info = {}
for plant in plants_rarity:
    plants_info[plant] = {}
    plants_info[plant]['rarity'] = plants_rarity[plant]
    if plant not in plants_rating:
        plants_info[plant]['rating'] = 0
    else:
        avg_rating = sum(plants_rating[plant]) / len(plants_rating[plant])
        plants_info[plant]['rating'] = avg_rating

plants_info = dict(sorted(plants_info.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating'])))

print('Plants for the exhibition:')
for plant in plants_info:
    rarity = plants_info[plant]['rarity']
    rating = plants_info[plant]['rating']
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")