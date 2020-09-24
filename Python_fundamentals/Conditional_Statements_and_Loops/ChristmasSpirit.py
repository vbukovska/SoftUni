quantity = int(input())
days = int(input())

ornament_price = 2
skirt_price = 5
garlands_price = 3
lights_price = 15

day = 0
spirit = 0
spent_money = 0

while day < days:
    day += 1
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        spent_money += quantity * ornament_price
        spirit += 5
    if day % 3 == 0:
        spent_money += quantity * skirt_price + quantity * garlands_price
        spirit += 13
    if day % 5 == 0:
        spent_money += quantity * lights_price
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        spent_money += skirt_price + garlands_price + lights_price

if days % 10 == 0:
    spirit -= 30

print(f'Total cost: {spent_money}')
print(f'Total spirit: {spirit}')
