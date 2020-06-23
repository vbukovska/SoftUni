from math import pi
figure = str(input())
if figure == 'square':
    side = float(input())
    area = round(side * side, 3)
    print(area)
elif figure == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    area = round(first_side*second_side, 3)
    print(area)
elif figure == 'circle':
    radius = float(input())
    area = round(pi * radius ** 2, 3)
    print(area)
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = round(side * height / 2, 3)
    print(area)
