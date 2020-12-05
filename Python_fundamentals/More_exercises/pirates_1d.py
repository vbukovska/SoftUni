cities = {}
while True:
    new_city = input()
    if new_city == 'Sail':
        break
    curr_city, curr_population, curr_gold = new_city.split('||')
    curr_population = int(curr_population)
    curr_gold = int(curr_gold)
    if curr_city not in cities:
        cities[curr_city] = {}
        cities[curr_city]['population'] = 0
        cities[curr_city]['treasure'] = 0
    cities[curr_city]['population'] += curr_population
    cities[curr_city]['treasure'] += curr_gold

while True:
    command_line = input()
    if command_line == 'End':
        break
    command_line = command_line.split('=>')
    if 'Plunder' in command_line:
        city = command_line[1]
        people_to_kill = int(command_line[2])
        gold_to_steal = int(command_line[3])
        cities[city]['population'] -= people_to_kill
        cities[city]['treasure'] -= gold_to_steal
        print(f"{city} plundered! {gold_to_steal} gold stolen, {people_to_kill} citizens killed.")
        if cities[city]['population'] == 0 or cities[city]['treasure'] == 0:
            print(f"{city} has been wiped off the map!")
            cities.pop(city)
    else:
        city = command_line[1]
        gold_achieved = int(command_line[2])
        if gold_achieved < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            cities[city]['treasure'] += gold_achieved
            print(f"{gold_achieved} gold added to the city treasury. {city} now has {cities[city]['treasure']} gold.")

if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    sorted_cities = dict(sorted(cities.items(), key=lambda x: (-x[1]['treasure'], x[0])))
    #sort by gold/treasure descending and then by name ascending cities = {city_name: {population:int, treasure:int}...}
    for city in sorted_cities:
        print(f"{city} -> Population: {sorted_cities[city]['population']} citizens, Gold: {sorted_cities[city]['treasure']} kg")
