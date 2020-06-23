budget = float(input())
actors = int(input())
clothes_price = float(input())

decor = budget * 0.1

if actors > 150:
    clothes_price = clothes_price * 0.9

costs_clothes = actors * clothes_price
total_cost = decor + costs_clothes
total = abs(budget - total_cost)

if total_cost <= budget:
    print('Action!')
    print(f'Wingard starts filming with {total:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total:.2f} leva more.')
