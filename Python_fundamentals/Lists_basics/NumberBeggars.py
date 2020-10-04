numbers = input().split(', ')
beggars = int(input())
list_of_beggars = [0] * beggars
curr_beggar = 0
for num in range(len(numbers)):
    if curr_beggar == beggars:
        curr_beggar = 1
    else:
        curr_beggar += 1
    list_of_beggars[curr_beggar-1] = list_of_beggars[curr_beggar-1] + int(numbers[num])

print(list_of_beggars)
