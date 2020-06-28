import math
year = input()
p = int(input())
h = int(input())

weekends = 48
play_in_sofia = (weekends - h) * 3 / 4 + p * 2 / 3
play_at_home = h

tot_play = play_in_sofia + play_at_home
if year == 'leap':
    tot_play = tot_play * 1.15
print(math.floor(tot_play))
