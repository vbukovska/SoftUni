n = int(input())
model = input()
delivery = input()

price = 0

if n < 10:
    print('Invalid order')
else:
    if model == '90X130':
        price = 110
        if n > 60:
            price *= 0.92
        elif n > 30:
            price *= 0.95
    elif model == '100X150':
        price = 140
        if n > 80:
            price *= 0.9
        elif n > 40:
            price *= 0.94
    elif model == '130X180':
        price = 190
        if n > 50:
            price *= 0.88
        elif n > 20:
            price *= 0.93
    elif model == '200X300':
        price = 250
        if n > 50:
            price *= 0.86
        elif n > 25:
            price *= 0.91

    tot_price = n * price
    if delivery == 'With delivery':
        tot_price += 60

    if n > 99:
        tot_price *= 0.96

    print(f'{tot_price:.2f} BGN')
