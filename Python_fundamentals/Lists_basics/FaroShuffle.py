cards = input().split(' ')
times = int(input())

for time in range(times):
    shuffled_list = []
    for i in range(0, (len(cards) // 2)):
        shuffled_list.append(cards[i])
        shuffled_list.append(cards[len(cards) // 2 + i])
    cards = shuffled_list

print(cards)
