record = float(input())  # seconds
distance = float(input())  # meters
speed = float(input())  # seconds/1m
flow_time = (distance // 15) * 12.5

time = speed * distance + flow_time
diff = abs(record - time)

if record <= time:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
else:
    print(f' Yes, he succeeded! The new world record is {time:.2f} seconds.')
