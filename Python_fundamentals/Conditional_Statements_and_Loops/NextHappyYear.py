num = int(input())
year = num
is_unique = True
while year >= num:
    year += 1
    happy_year = str(year)
    is_unique = True
    for i in range(len(happy_year)-1):
        for j in range(i+1, len(happy_year)):
            if happy_year[j] == happy_year[i]:
                is_unique = False
                break
            else:
                continue
        if not is_unique:
            break
    if is_unique:
        break

print(year)

