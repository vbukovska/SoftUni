legendary = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary_item = None
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

while True:
    materials = input().split()
    for index in range(1, len(materials), 2):
        material = materials[index].lower()
        quantity = int(materials[index - 1])
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                legendary_item = legendary[material]
                key_materials[material] -= 250
                break
        elif material in junk:
            junk[material] += quantity
        else:
            junk[material] = quantity
    if legendary_item:
        break

print(f'{legendary_item} obtained!')
key_materials = dict(sorted(dict(sorted(key_materials.items(), key=lambda x: x[0])).items(), key=lambda y: y[1], reverse=True))
[print(f"{key}: {value}")for key, value in key_materials.items()]
[print(f"{key}: {value}") for key, value in dict(sorted(junk.items(), key=lambda z: z[0])).items()]


# [print(f"{key}: {value}") for key, value in dict(sorted(dict(sorted(key_materials.items(), key = lambda x: x[1])).items(), key = lambda y: y[0])).items()]