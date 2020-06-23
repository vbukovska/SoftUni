price_puzzle = 2.6
price_doll = 3
price_teddy_bear = 4.1
price_minion = 8.2
price_truck = 2
price_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
order_number = number_dolls + number_puzzles + number_minions + number_teddy_bears + number_trucks
sum_puzzles = number_puzzles * price_puzzle
sum_dolls = number_dolls * price_doll
sum_teddy_bears = number_teddy_bears * price_teddy_bear
sum_minions = number_minions * price_minion
sum_trucks = number_trucks * price_truck
total_order = sum_puzzles + sum_dolls + sum_teddy_bears + sum_minions + sum_trucks

if order_number >= 50:
    total_order = total_order - total_order * 0.25
profit = total_order - total_order * 0.1

if profit >= price_excursion:
    left_money = round(profit - price_excursion, 3)
    print(f'Yes! {left_money:.2f} lv left.')
else:
    lack = round(price_excursion - profit, 3)
    print(f'Not enough money! {lack:.2f} lv needed.')
