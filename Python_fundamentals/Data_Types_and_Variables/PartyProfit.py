party_size = int(input())
days = int(input())

total_money = 0

for i in range(1, days+1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    total_money += 50 - party_size * 2
    if i % 3 == 0:
        total_money -= 3 * party_size
    if i % 5 == 0:
        total_money += 20 * party_size
        if i % 3 == 0:
            total_money -= 2 * party_size
print(f'{party_size} companions received {total_money // party_size} coins each.')

