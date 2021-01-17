# working solution
from collections import deque
sequence = input()
parentheses_dict = {'(': ')', '[': ']', '{': '}'}
stack_open = []
sequence_que = deque(sequence)
is_balanced = False
for index in range(len(sequence_que)):
    element = sequence_que.popleft()
    if element in parentheses_dict:
        stack_open.append(element)
    elif stack_open:
        curr_bracket = stack_open.pop()
        if element == parentheses_dict[curr_bracket]:
            is_balanced = True
            continue
        else:
            is_balanced = False
            break
    else:
        is_balanced = False
        break
if stack_open:
    is_balanced = False
if is_balanced:
    print('YES')
else:
    print('NO')
