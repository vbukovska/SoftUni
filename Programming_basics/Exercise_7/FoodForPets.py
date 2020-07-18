days = int(input())
tot_food = float(input())

tot_dog_food_food = 0
tot_cat_food = 0
tot_dog_food = 0
tot_dog_bisquits = 0
tot_cat_bisquits = 0
counter = 0

for i in range(1, days+1):
    dog_food = int(input())
    cat_food = int(input())
    tot_dog_food += dog_food
    tot_cat_food += cat_food
    counter += 1
    if counter == 3:
        tot_dog_bisquits += dog_food * 0.1
        tot_cat_bisquits += cat_food * 0.1
        counter = 0
print(f'Total eaten biscuits: {round(tot_cat_bisquits + tot_dog_bisquits)}gr.')
print(f'{((tot_dog_food + tot_cat_food) / tot_food) * 100:.2f}% of the food has been eaten.')
print(f'{(tot_dog_food / (tot_dog_food + tot_cat_food) ) * 100:.2f}% eaten from the dog.')
print(f'{(tot_cat_food / (tot_dog_food + tot_cat_food) ) * 100:.2f}% eaten from the cat.')

