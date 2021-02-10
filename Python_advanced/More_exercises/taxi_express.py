from collections import deque

customers = deque([int(c) for c in input().split(", ")])
taxis = [int(t) for t in input().split(", ")]
total_time = 0
while customers:
    curr_customer = customers[0]
    while taxis:
        curr_taxi = taxis.pop()
        if curr_taxi >= curr_customer:
            total_time += curr_customer
            customers.popleft()
            break
    if not taxis:
        break

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(c) for c in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
