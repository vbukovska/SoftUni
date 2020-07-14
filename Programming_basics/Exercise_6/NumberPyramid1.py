n = int(input())
k = 1
is_done = False
for row in range(1, n + 1):  # row
    start = k
    for m in range(k, start + row):  # number of digits
        if m == start + row - 1:
            print(m)
            if m == n:
                is_done = True
            k += 1
            break
        else:
            print(m, end=' ')
        if k == n:
            is_done = True
            break
        k += 1
    if is_done:
        break
