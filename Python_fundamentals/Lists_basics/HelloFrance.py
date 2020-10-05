items_collection = input().split('|')
budget = float(input())
items_info = []
bought_items = []
for i in range(len(items_collection)):
    items_info.append(items_collection[i].split('->'))

for item in range(len(items_info)):
    if items_info[item][0] == 'Clothes':
        price = float(items_info[item][1])
        if price <= min(budget, 50.00):
            budget -= price
            bought_items.append(price*1.4)
    elif items_info[item][0] == 'Shoes':
        price = float(items_info[item][1])
        if price <= min(budget, 35.00):
            budget -= price
            bought_items.append(price*1.4)
    else:
        price = float(items_info[item][1])
        if price <= min(budget, 20.50):
            budget -= price
            bought_items.append(price*1.4)
for i in range(len(bought_items)):
    if i == len(bought_items) - 1:
        print(f'{bought_items[i]:.2f}')
    else:
        print(f'{bought_items[i]:.2f}', end=' ')

profit = sum(bought_items) - sum(bought_items)/1.4
print(f'Profit: {profit:.2f}')
if sum(bought_items) + budget >= 150.00:

    print('Hello, France!')
else:
    print('Time to go.')
