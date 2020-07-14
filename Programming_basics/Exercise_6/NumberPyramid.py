n = int(input())
is_done = False
m = 1
for row in range(1, n + 1):
    for i in range(1, row+1):
        if i == row:
            print(m)
        else:
            print(m, end=' ')
        if m == n:
            is_done = True
            break
        m += 1
    if is_done:
        break
