products = {}

while True:
    command_line = input()
    if command_line == 'buy':
        break
    name, price, quantity = command_line.split()
    price = float(price)
    quantity = int(quantity)
    if name in products:
        products[name][0] = price
        products[name][1] += quantity
    else:
        products[name] = [price, quantity]

for product in products:
    tot_price = products[product][0] * products[product][1]
    print(f"{product} -> {tot_price:.2f}")

