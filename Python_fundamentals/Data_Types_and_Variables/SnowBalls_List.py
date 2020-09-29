tot_balls = int(input())

best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0
curr_ball = {'snow': 0, 'time': 0, 'quality': 0, 'value': 0}
best_ball = curr_ball
for ball in range(1, tot_balls + 1):
    curr_ball['snow'] = int(input())
    curr_ball['time'] = int(input())
    curr_ball['quality'] = int(input())
    curr_ball['value'] = int((curr_ball['snow'] / curr_ball['time']) ** curr_ball['quality'])
    if best_ball['value'] < curr_ball['value']:
        best_ball = curr_ball #not working best_ball and curr_ball points to the same object and get modified together every time I read from the console.
print(best_ball)
#print(f'{best_ball['snow']} : {best_snowball_time} = {best_snowball_value} ({best_snowball_quality})')

