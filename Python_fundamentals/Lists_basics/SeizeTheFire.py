fires = input().split('#')
water = int(input())
fires_info = []

for i in range(len(fires)):
    fires_info.append(fires[i].split(' = '))
    fires_info[i][1] = int(fires_info[i][1])
print(fires_info)
print(type(fires_info[0][1]))
effort = 0
seized_fires = []

for fire in range(len(fires_info)):
    if fires_info[fire][0] == 'High':
        if 81 <= fires_info[fire][1] <= min(water, 125):
            seized_fires.append(fires_info[fire][1])
            effort += fires_info[fire][1] * 0.25
            water -= fires_info[fire][1]
        else:
            continue
    elif fires_info[fire][0] == 'Medium':
        if 51 <= fires_info[fire][1] <= min(water, 80):
            seized_fires.append(fires_info[fire][1])
            effort += fires_info[fire][1] * 0.25
            water -= fires_info[fire][1]
        else:
            continue
    elif fires_info[fire][0] == 'Low':
        if 1 <= fires_info[fire][1] <= min(water, 50):
            seized_fires.append(fires_info[fire][1])
            effort += fires_info[fire][1] * 0.25
            water -= fires_info[fire][1]
        else:
            continue
    if water == 0:
        break
print('Cells:')
for i in range(len(seized_fires)):
    print(f'- {seized_fires[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(seized_fires)}')
