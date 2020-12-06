number_heroes = int(input())

hp_points = {}
mana_points = {}

for _ in range(number_heroes):
    hero_name, hero_hp, hero_mana = input().split()
    hero_hp = int(hero_hp)
    hero_mana = int(hero_mana)
    hero_hp = min(100, hero_hp)
    hp_points[hero_name] = hero_hp
    hero_mana = min(200, hero_mana)
    mana_points[hero_name] = hero_mana

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        hero = command[1]
        required_mana = int(command[2])
        spell_name = command[3]
        if mana_points[hero] >= required_mana:
            mana_points[hero] -= required_mana
            print(f"{hero} has successfully cast {spell_name} and now has {mana_points[hero]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command[0] == 'TakeDamage':
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        hp_points[hero] -= damage
        if hp_points[hero] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hp_points[hero]} HP left!")
        else:
            hp_points.pop(hero)
            mana_points.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif command[0] == 'Recharge':
        hero = command[1]
        mana_gain = int(command[2])
        if mana_points[hero] + mana_gain > 200:
            mana_gain = 200 - mana_points[hero]
        mana_points[hero] += mana_gain
        print(f"{hero} recharged for {mana_gain} MP!")
    else:
        hero = command[1]
        hp_gain = int(command[2])
        if hp_points[hero] + hp_gain > 100:
            hp_gain = 100 - hp_points[hero]
        hp_points[hero] += hp_gain
        print(f"{hero} healed for {hp_gain} HP!")

sorted_hp_points = dict(sorted(hp_points.items(), key=lambda x: (-x[1], x[0])))
for hero, hp in sorted_hp_points.items():
    print(hero)
    print(f"  HP: {hp}")
    print(f"  MP: {mana_points[hero]}")
