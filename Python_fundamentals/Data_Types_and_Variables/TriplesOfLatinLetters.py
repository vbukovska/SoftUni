n = int(input())

for char_1 in range(97, 97 + n):
    for char_2 in range(97, 97 + n):
        for char_3 in range(97, 97 + n):
            print(f'{chr(char_1)}{chr(char_2)}{chr(char_3)}')

