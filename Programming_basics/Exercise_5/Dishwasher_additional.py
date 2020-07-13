number_bottles = int(input())

bottles_detergent = number_bottles * 750
plate_detergent = 5
pot_detergent = 15
plates = 0
pots = 0
counter = 0
command = input()
while command != 'End':
    dishes = int(command)
    counter += 1
    if counter % 3 == 0:
        bottles_detergent -= dishes * pot_detergent
        pots += dishes
    else:
        bottles_detergent -= dishes * plate_detergent
        plates += dishes
    if bottles_detergent <= 0:
        break
    command = input()

if bottles_detergent >= 0:
    print('Detergent was enough!')
    print(f'{plates} dishes and {pots} were washed.')
    print(f'Leftover detergent {bottles_detergent} ml.')
else:
    print(f'Not enough detergent, {abs(bottles_detergent)} ml. more necessary!')

