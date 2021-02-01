def combinations(n, people, combos=[]):
    if len(combos) == n:
        print(', '.join(combos))
        return
    for i in range(len(people)):
        combos.append(people[i])
        combinations(n, people[i + 1:], combos)
        combos.pop()


names = input().split(", ")
chairs = int(input())

combinations(chairs, names)
