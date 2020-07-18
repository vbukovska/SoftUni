n = int(input())

points = 0
n_red = 0
n_orange = 0
n_yellow = 0
n_white = 0
n_black = 0
n_other = 0

for i in range(1, n+1):
    ball_colour = input()
    if ball_colour == 'red':
        points += 5
        n_red += 1
    elif ball_colour == 'orange':
        points += 10
        n_orange += 1
    elif ball_colour == 'yellow':
        points += 15
        n_yellow += 1
    elif ball_colour == 'white':
        points += 20
        n_white += 1
    elif ball_colour == 'black':
        points /= 2
        n_black += 1
    else:
        n_other += 1
        continue

print(f'Total points: {int(points)}')
print(f'Points from red balls: {n_red}')
print(f'Points from orange balls: {n_orange}')
print(f'Points from yellow balls: {n_yellow}')
print(f'Points from white balls: {n_white}')
print(f'Other colors picked: {n_other}')
print(f'Divides from black balls: {n_black}')
