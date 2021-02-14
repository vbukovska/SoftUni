def stock_availability(inventory, command, *args):
    attributes = args
    if command == "delivery":
        inventory.extend(attributes)
    else:
        if not attributes:
            inventory.pop(0)
        else:
            if isinstance(attributes[0], int):
                boxes_to_sell = attributes[0]
                for index in range(boxes_to_sell):
                    inventory.pop(0)
            else:
                for order in attributes:
                    while order in inventory:
                        stock_index = inventory.index(order)
                        inventory.pop(stock_index)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
