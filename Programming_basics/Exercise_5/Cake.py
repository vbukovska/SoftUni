width = int(input())
length = int(input())
cake_size = width * length
tot_pieces = 0
command = input()
while command != 'STOP':
    tot_pieces += int(command)
    if tot_pieces >= cake_size:
        print(f'No more cake left! You need {tot_pieces - cake_size} pieces more.')
        break
    command = input()

if command == 'STOP':
    print(f'{cake_size - tot_pieces} pieces are left.')
