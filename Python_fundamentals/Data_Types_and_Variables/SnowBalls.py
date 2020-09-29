tot_balls = int(input())

best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0
for curr_snowball in range(1, tot_balls + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    if best_snowball_value < snowball_value:
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
        best_snowball_value = snowball_value
print(f'{best_snowball_snow} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})')

