days = int(input())
place = input()
rating = input()

room_price = 18
apartment_price = 25
president_apartment_price = 35

price = 0
discount = 0

if place == 'apartment':
    price = apartment_price
    if days-1 <= 10:
        discount = 0.3
    elif days-1 <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif place == 'president apartment':
    price = president_apartment_price
    if days-1 <= 10:
        discount = 0.1
    elif days-1 <= 15:
        discount = 0.15
    else:
        discount = 0.2
else:
    price = room_price

if rating == 'negative':
    total_price = price * (days - 1) * (1 - discount) * 0.9
else:
    total_price = price * (days - 1) * (1 - discount) * 1.25

print(f'{total_price:.2f}')
