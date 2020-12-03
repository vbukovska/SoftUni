import re

pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$"
orders = []
total_price = 0
while True:
    data = input()
    if data == 'Purchase':
        break
    match = re.match(pattern, data)
    if match:
        obj = match.groupdict()
        orders.append(obj["name"])
        total_price += float(obj["price"]) * int(obj["quantity"])
    # order = re.finditer(pattern, data)
    # order = [curr_order.groupdict() for curr_order in order]
    # if order:
    #     order = order[0]
    #     orders.append(order['name'])
    #     total_price += float(order['price']) * int(order['quantity'])

print('Bought furniture:')
for name in orders:
    print(name)
print(f'Total money spend: {total_price:.2f}')