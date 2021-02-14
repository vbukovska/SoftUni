from collections import deque

effects = deque(int(x) for x in input().split(", "))
powers = [int(y) for y in input().split(", ")]
crafted_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
is_enough = {}
for firework in crafted_fireworks.keys():
    is_enough[firework] = False

while powers:
    curr_power = powers[-1]
    if curr_power <= 0:
        powers.pop()
        continue
    while effects:
        curr_effect = effects[0]
        if curr_effect <= 0:
            effects.popleft()
            continue
        curr_sum = curr_effect + curr_power
        if curr_sum % 15 == 0:
            crafted_fireworks["Crossette Fireworks"] += 1
            effects.popleft()
            powers.pop()
            if crafted_fireworks["Crossette Fireworks"] == 3:
                is_enough["Crossette Fireworks"] = True
            break
        elif curr_sum % 3 == 0:
            crafted_fireworks["Palm Fireworks"] += 1
            effects.popleft()
            powers.pop()
            if crafted_fireworks["Palm Fireworks"] == 3:
                is_enough["Palm Fireworks"] = True
            break
        elif curr_sum % 5 == 0:
            crafted_fireworks["Willow Fireworks"] += 1
            effects.popleft()
            powers.pop()
            if crafted_fireworks["Willow Fireworks"] == 3:
                is_enough["Willow Fireworks"] = True
            break
        else:
            effects[0] -= 1
            curr_effect = effects.popleft()
            effects.append(curr_effect)
    if all(is_enough.values()):
        break
    if not effects:
        break

if all(is_enough.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join([str(effects.popleft()) for i in range(len(effects))])}")

if powers:
    powers_left = []
    for power in range(len(powers)):
        last_power = powers.pop()
        powers_left.insert(0, last_power)
    print(f"Explosive Power left: {', '.join([str(p) for p in powers_left])}")

for firework, amount in crafted_fireworks.items():
    print(f"{firework}: {amount}")


