from collections import deque

que = deque()

while True:
    customer = input()
    if customer == 'End':
        print(f'{len(que)} people remaining.')
        break
    elif customer == 'Paid':
        while que:
            print(que.popleft())
    else:
        que.append(customer)