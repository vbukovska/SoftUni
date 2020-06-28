month = input()
overnight = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if overnight > 14:
        studio_price = studio_price * 0.7
        apartment_price = apartment_price * 0.9
    elif overnight > 7:
        studio_price = studio_price * 0.95

elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if overnight > 14:
        studio_price = studio_price * 0.8
        apartment_price = apartment_price * 0.9
else:
    studio_price = 76
    apartment_price = 77
    if overnight > 14:
        apartment_price = apartment_price * 0.9


print(f'Apartment: {overnight * apartment_price:.2f} lv.')
print(f'Studio: {overnight * studio_price:.2f} lv.')
