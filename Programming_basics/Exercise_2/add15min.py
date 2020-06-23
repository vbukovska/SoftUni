hour = int(input())
minutes = int(input())

add_time = 15
minutes_temp = minutes + add_time
minutes = minutes_temp % 60
hour = hour + minutes_temp // 60

if hour == 24:
    hour = 0

if minutes <= 9:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
