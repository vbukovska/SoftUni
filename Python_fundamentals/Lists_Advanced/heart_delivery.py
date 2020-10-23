valentines = [int(el) for el in input().split('@')]
curr_index = 0
while True:
    command_line = input().split()
    command = command_line[0]
    if command == 'Love!':
        print(f'Cupid\'s last position was {curr_index}.')
        not_succeeded = [hearts for hearts in valentines if not hearts == 0]
        if len(not_succeeded) == 0:
            print('Mission was successful.')
        else:
            print(f'Cupid has failed {len(not_succeeded)} places.')
        break
    else:
        jump = int(command_line[1])
        if curr_index + jump > len(valentines) - 1:
            curr_index = 0
        else:
            curr_index += jump
        if valentines[curr_index] == 0:
            print(f'Place {curr_index} already had Valentine\'s day.')
        else:
            valentines[curr_index] -= 2
            if valentines[curr_index] == 0:
                print(f'Place {curr_index} has Valentine\'s day.')
