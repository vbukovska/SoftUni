days = int(input())
number_confectioners = int(input())
number_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())

cakes_price = 45
waffles_price = 5.8
pancakes_price = 3.2

sum_cakes = number_cakes * cakes_price
sum_waffles = number_waffles * waffles_price
sum_pancakes = number_pancakes * pancakes_price

sumPerDay = (sum_cakes + sum_waffles + sum_pancakes) * number_confectioners
totSum = sumPerDay * days
finalSum = 7/8 * totSum
print(finalSum)
