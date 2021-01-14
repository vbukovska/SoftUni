from collections import deque

children = input().split()
step = int(input())

children_que = deque(children)


index = 0
while len(children_que) > 1:
    index += 1
    if index == step:
        print(f'Removed {children_que.popleft()}')
        index = 0
    else:
        children_que.append(children_que.popleft())
print(f'Last is {children_que[0]}')