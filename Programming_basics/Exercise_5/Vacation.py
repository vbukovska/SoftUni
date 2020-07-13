vacation_money = float(input())
currency = float(input())

sequence_spend = 0
tot_days = 0
last_time = 0
is_failed = False

while currency < vacation_money:
    action = input()
    money = float(input())

    if action == 'spend':
        currency -= money
        if currency < 0:
            currency = 0

        tot_days += 1
        if tot_days - last_time == 1:
            sequence_spend += 1
        else:
            sequence_spend = 1
        last_time = tot_days
        if sequence_spend == 5:
            is_failed = True
            print(f"You can't save the money.")
            print(tot_days)
            break
    else:
        currency += money
        tot_days += 1

if not is_failed:
    print(f'You saved the money for {tot_days} days.')



