charity_amount = int(input())

tot_amount = 0
is_cash = True
cash_amount = 0
card_amount = 0
cash_counter = 0
card_counter = 0

command = input()
while command != 'End':
    amount = int(command)
    if not is_cash:
        is_cash = True
        if amount < 10:
            print('Error in transaction!')
            command = input()
            continue
        tot_amount += amount
        card_amount += amount
        card_counter += 1
        print('Product sold!')
    else:
        is_cash = False
        if amount > 100:
            print('Error in transaction!')
            command = input()
            continue
        tot_amount += amount
        cash_amount += amount
        cash_counter += 1
        print('Product sold!')
    if tot_amount >= charity_amount:
        print(f'Average CS: {cash_amount / card_counter:.2f}')
        print(f'Average CC: {card_amount / card_counter:.2f}')
        break
    command = input()

if command == 'End':
    print('Failed to collect required money for charity.')
