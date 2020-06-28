type_flowers = input()
number_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiola_price = 2.5

tot_price = 0

if type_flowers == 'Roses':
    if number_flowers > 80:
        rose_price = rose_price * 0.9
    tot_price = number_flowers * rose_price
elif type_flowers == 'Dahlias':
    if number_flowers > 90:
        dahlia_price = dahlia_price * 0.85
    tot_price = number_flowers * dahlia_price
elif type_flowers == 'Tulips':
    if number_flowers > 80:
        tulip_price = tulip_price * 0.85
    tot_price = number_flowers * tulip_price
elif type_flowers == 'Narcissus':
    if number_flowers < 120:
        narcissus_price = narcissus_price * 1.15
    tot_price = number_flowers * narcissus_price
else:
    if number_flowers < 80:
        gladiola_price = gladiola_price * 1.2
    tot_price = number_flowers * gladiola_price

residue = budget - tot_price

if residue >= 0:
    print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {abs(residue):.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(residue):.2f} leva more.')
