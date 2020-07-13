tot_food = int(input()) * 1000
food_eaten = 0
while True:
    command = input()
    if command == 'Adopted':
        break
    food_eaten += int(command)


if food_eaten <= tot_food:
    print(f'Food is enough! Leftovers: {tot_food - food_eaten} grams.')
else:
    print(f'Food is not enough. You need {food_eaten - tot_food} grams more.')
