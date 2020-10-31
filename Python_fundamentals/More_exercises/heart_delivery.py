required_love = [int(el) for el in input().split('@')]
curr_index = 0
while True:
    command_line = input().split()
    if 'Love!' in command_line:
        break
    jump_length = int(command_line[1])
    curr_index += jump_length
    if curr_index >= len(required_love):
        curr_index = 0
    if required_love[curr_index] > 0:
        required_love[curr_index] -= 2
        if required_love[curr_index] == 0:
            print(f"Place {curr_index} has Valentine's day.")
    elif required_love[curr_index] == 0:
        print(f"Place {curr_index} already had Valentine's day.")

print(f"Cupid's last position was {curr_index}.")
no_valentine_houses = len([house for house in required_love if house > 0])
if no_valentine_houses == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {no_valentine_houses} places.')