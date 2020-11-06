worker_daily_production = int(input())
workers = int(input())
competing_production = int(input())

total_daily_production = worker_daily_production * workers
total_production = 0

for day in range(1, 31):
    if day % 3 == 0:
        total_production += (total_daily_production * 75) // 100
    else:
        total_production += total_daily_production

print(f'You have produced {total_production} biscuits for the past month.')
compete_result = (total_production / competing_production - 1) * 100
if compete_result > 0:
    print(f'You produce {compete_result:.2f} percent more biscuits.')
else:
    print(f'You produce {abs(compete_result):.2f} percent less biscuits.')
