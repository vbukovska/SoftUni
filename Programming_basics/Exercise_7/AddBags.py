price_luggage = float(input())
kg_luggage = float(input())
days = int(input())
num_luggage = int(input())

total_price = 0

if kg_luggage > 20:
    total_price += price_luggage
elif kg_luggage >= 10:
    total_price += price_luggage * 0.5
else:
    total_price += price_luggage * 0.2

if days > 30:
    total_price *= 1.1
elif days >= 7:
    total_price *= 1.15
else:
    total_price *= 1.4

total = total_price * num_luggage

print(f'The total price of bags is: {total:.2f} lv. ')
