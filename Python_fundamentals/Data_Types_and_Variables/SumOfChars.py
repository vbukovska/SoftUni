lines = int(input())

char_sum = 0

for i in range(1, lines+1):
    char_sum += ord(input())
print(f'The sum equals: {char_sum}')
