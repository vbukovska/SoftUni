budget = int(input())
season = input()
number_fisherman = int(input())

ship_price = 0
discount = 0

if season == 'Spring':
    ship_price = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_price = 4200
else:
    ship_price = 2600

if number_fisherman <= 6:
    discount = 0.1
elif 7 <= number_fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

ship_price = ship_price * (1-discount)

if number_fisherman % 2 == 0 and season != 'Autumn':
    ship_price = ship_price * 0.95

residue = budget - ship_price

if residue >= 0:
    print(f'Yes! You have {abs(residue):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(residue):.2f} leva.')
