budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = 0.25 * (flour_price * 1.25)

cozonac_price = flour_price + eggs_price + milk_price

current_Cozonacs_count = 0
colored_eggs = 0
money_spent = 0

while current_Cozonacs_count < budget // cozonac_price:
    money_spent += cozonac_price
    current_Cozonacs_count += 1
    colored_eggs += 3
    if current_Cozonacs_count % 3 == 0:
        colored_eggs -= (current_Cozonacs_count - 2)

print(f'You made {current_Cozonacs_count} cozonacs! Now you have {colored_eggs} eggs and {(budget - money_spent):.2f}BGN left.')
