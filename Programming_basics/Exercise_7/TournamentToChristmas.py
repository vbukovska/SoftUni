days = int(input())
tot_wins = 0
tot_loses = 0
dayly_money = 0
tot_money = 0
for i in range(1, days + 1):
    wins = 0
    loses = 0
    dayly_money = 0
    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()
        if result == 'win':
            wins += 1
            dayly_money += 20
        else:
            loses += 1
    if wins > loses:
        dayly_money += dayly_money * 0.1
        tot_wins += 1
    else:
        tot_loses += 1
    tot_money += dayly_money
if tot_wins > tot_loses:
    tot_money += tot_money * 0.2
    print(f'You won the tournament! Total raised money: {tot_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {tot_money:.2f}')
