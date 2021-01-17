from collections import deque

food_quantity = int(input())
orders_list = [int(order) for order in input().split()]

orders = deque(orders_list)

max_order = 0
number_of_orders = len(orders)
for curr_order in orders:
    if curr_order > max_order:
        max_order = curr_order
for _ in range(len(orders)):
    curr_order = orders[0]
    if food_quantity >= curr_order:
        food_quantity -= curr_order
        orders.popleft()
    else:
        break

print(max_order)
if orders:
    print(f"Orders left: {' '.join([str(orders.popleft()) for _ in range(len(orders))])}")
else:
    print('Orders complete')
