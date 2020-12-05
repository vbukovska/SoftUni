treasure = {}
population = {}
while True:
    new_city = input()
    if new_city == 'Sail':
        break
    curr_city, curr_population, curr_gold = new_city.split('||')
    curr_population = int(curr_population)
    curr_gold = int(curr_gold)
    if curr_city not in treasure:
        treasure[curr_city] = 0
        population[curr_city] = 0
    population[curr_city] += curr_population
    treasure[curr_city] += curr_gold

while True:
    command_line = input()
    if command_line == 'End':
        break
    command_line = command_line.split('=>')
    if 'Plunder' in command_line:
        city = command_line[1]
        people_to_kill = int(command_line[2])
        gold_to_steal = int(command_line[3])
        population[city] -= people_to_kill
        treasure[city] -= gold_to_steal
        print(f"{city} plundered! {gold_to_steal} gold stolen, {people_to_kill} citizens killed.")
        if population[city] == 0 or treasure[city] == 0:
            print(f"{city} has been wiped off the map!")
            treasure.pop(city)
            population.pop(city)
    else:
        city = command_line[1]
        gold_achieved = int(command_line[2])
        if gold_achieved < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            treasure[city] += gold_achieved
            print(f"{gold_achieved} gold added to the city treasury. {city} now has {treasure[city]} gold.")

if len(treasure) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(treasure)} wealthy settlements to go to:")
    sorted_treasure = dict(sorted(treasure.items(), key=lambda x: (-x[1], x[0])))
    for city in sorted_treasure:
        print(f"{city} -> Population: {population[city]} citizens, Gold: {sorted_treasure[city]} kg")
