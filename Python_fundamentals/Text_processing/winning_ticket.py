def check_for_sequence(half_ticket):
    curr_symbol = ''
    counter = 0
    for character in half_ticket:
        if character == curr_symbol:
            counter += 1
            continue
        elif counter >= 6:
            break
        if character in winning_symbols:
            curr_symbol = character
            counter = 1
    return {'symbol': curr_symbol, 'length': counter}


tickets = input().split(', ')

winning_symbols = ['@', '#', '$', '^']

for index, ticket in enumerate(tickets):
    ticket = ticket.strip()
    if not ticket:
        continue
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    else:
        left_side = check_for_sequence(ticket[index:10])
        right_side = check_for_sequence(ticket[10:20])
    if left_side['symbol'] == right_side['symbol']:
        min_lenght = min(left_side['length'], right_side['length'])
        if 6 <= min_lenght <= 9:
            print(f'ticket "{ticket}" - {min_lenght}{left_side["symbol"]}')
        elif min_lenght == 10:
            print(f'ticket "{ticket}" - {left_side["length"]}{left_side["symbol"]} Jackpot!')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'ticket "{ticket}" - no match')
