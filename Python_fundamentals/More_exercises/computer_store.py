commands = ['special', 'regular']
tax = 0.2
price_list = []
while True:
    cmd = input()
    if cmd in commands:
        break
    curr_price = float(cmd)
    if curr_price <= 0:
        print('Invalid price!')
        continue
    else:
        price_list.append(curr_price)
price = sum(price_list)
taxes = price * 0.2
# sum(list(map(lambda x: x * 0.2, price_list)))
tot_price = price + taxes

if cmd == 'special':
    tot_price -= tot_price * 0.1
if tot_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {tot_price:.2f}$")
