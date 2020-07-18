tot_dog_food_kg = int(input())
tot_dog_food_g = tot_dog_food_kg * 1000
dog_food_eaten = 0
while True:
    command = input()
    if command == 'Adopted':
        break
    dog_food_eaten += int(command)
if tot_dog_food_g >= dog_food_eaten:
    print(f'Food is enough! Leftovers: {tot_dog_food_g - dog_food_eaten} grams.')
else:
    print(f'Food is not enough. You need {dog_food_eaten - tot_dog_food_g} grams more.')
