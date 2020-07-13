change = float(input())

change = round(change * 100, 2)
coin = 0
tot_coins = 0

while change > 0:
    coin = change // 200
    if coin > 0:
        change -= coin * 200
        tot_coins += coin
        continue
    coin = change // 100
    if coin > 0:
        change -= coin * 100
        tot_coins += coin
        continue
    coin = change // 50
    if coin > 0:
        change -= coin * 50
        tot_coins += coin
        continue
    coin = change // 20
    if coin > 0:
        change -= coin * 20
        tot_coins += coin
        continue
    coin = change // 10
    if coin > 0:
        change -= coin * 10
        tot_coins += coin
        continue
    coin = change // 5
    if coin > 0:
        change -= coin * 5
        tot_coins += coin
        continue
    coin = change // 2
    if coin > 0:
        change -= coin * 2
        tot_coins += coin
        continue
    coin = change // 1
    if coin > 0:
        change -= coin * 1
        tot_coins += coin
        continue
print(int(tot_coins))
