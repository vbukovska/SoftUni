age = int(input())
washing_price = float(input())
toy_price = int(input())

money = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money += (i * 10)/2 - 1
    else:
        money += toy_price

if money >= washing_price:
    print(f'Yes! {(money - washing_price):.2f}')
else:
    print(f'No! {(washing_price - money):.2f}')

