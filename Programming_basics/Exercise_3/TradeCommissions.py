city = input()
sales = float(input())

commission = 0
is_error = sales < 0 or (city != 'Sofia' and city != 'Varna' and city != 'Plovdiv')

if is_error:
    print('error')
else:
    if 0 < sales <= 500:
        if city == 'Sofia':
            commission = sales * 0.05
        elif city == 'Varna':
            commission = sales * 0.045
        else:
            commission = sales * 0.055
    elif 500 < sales <= 1000:
        if city == 'Sofia':
            commission = sales * 0.07
        elif city == 'Varna':
            commission = sales * 0.075
        else:
            commission = sales * 0.08
    elif 1000 < sales <= 10000:
        if city == 'Sofia':
            commission = sales * 0.08
        elif city == 'Varna':
            commission = sales * 0.1
        else:
            commission = sales * 0.12
    else:
        if city == 'Sofia':
            commission = sales * 0.12
        elif city == 'Varna':
            commission = sales * 0.13
        else:
            commission = sales * 0.145

    print(f'{commission:.2f}')