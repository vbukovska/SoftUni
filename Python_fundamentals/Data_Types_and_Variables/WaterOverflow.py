input_number = int(input())

capacity = 255
tot_water = 0

for i in range(1, input_number+1):
    liters = int(input())
    if not tot_water + liters > capacity:
        tot_water += liters
    else:
        print('Insufficient capacity!')
        continue
print(tot_water)
