even_string = input().split('|')
energy = 100
coins = 100
events = []
handled_events = 0
for i in range(len(even_string)):
    events.append(even_string[i].split('-'))


for event in range(len(events)):
    if events[event][0] == 'rest':
        handled_events += 1
        add_energy = min(100-energy, int(events[event][1]))
        energy += add_energy
        print(f'You gained {add_energy} energy.')
        print(f'Current energy: {energy}.')
    elif events[event][0] == 'order':
        handled_events += 1
        if energy >= 30:
            coins += int(events[event][1])
            energy -= 30
            print(f'You earned {int(events[event][1])} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        coins -= int(events[event][1])
        if coins > 0:
            handled_events += 1
            print(f'You bought {events[event][0]}.')
        else:
            print(f'Closed! Cannot afford {events[event][0]}.')
            break

if handled_events == len(events):
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
