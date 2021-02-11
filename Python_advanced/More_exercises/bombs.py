from collections import deque


bomb_effects = deque([int(n) for n in input().split(", ")])
bomb_casings = [int(m) for m in input().split(", ")]
BOMBS_LIB = {40: "Datura Bombs", 60: "Cherry Bombs", 120: "Smoke Decoy Bombs"}
crafted = {}
is_filled_poach = {}
for bomb in BOMBS_LIB.values():
    is_filled_poach[bomb] = False
    crafted[bomb] = 0

while bomb_effects:
    curr_effect = bomb_effects[0]
    while bomb_casings:
        curr_casing = bomb_casings[-1]
        curr_mix = curr_effect + curr_casing
        if curr_mix in BOMBS_LIB:
            bomb_casings.pop()
            bomb_effects.popleft()
            curr_craft = BOMBS_LIB[curr_mix]
            if curr_craft not in crafted:
                crafted[curr_craft] = 0
            crafted[curr_craft] += 1
            if curr_craft not in is_filled_poach:
                is_filled_poach[curr_craft] = False
            if crafted[curr_craft] >= 3:
                is_filled_poach[curr_craft] = True
            break
        bomb_casings[-1] -= 5
        if bomb_casings[-1] == 0:
            bomb_casings.pop()
    if all(is_filled_poach.values()):
        break
    if not bomb_casings:
        break

if all(is_filled_poach.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([ str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(y) for y in bomb_casings])}")
else:
    print("Bomb Casings: empty")
crafted = dict(sorted(crafted.items(), key=lambda x: x[0]))
for key, value in crafted.items():
    print(f"{key}: {value}")



