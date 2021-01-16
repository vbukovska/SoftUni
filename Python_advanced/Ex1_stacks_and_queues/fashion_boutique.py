clothes = [int(i) for i in input().split()]
capacity = int(input())

clothes_stack = []
racks_number = 1
rack_capacity = capacity

for cloth in clothes:
    clothes_stack.append(cloth)


while clothes_stack:
    current_clothes = clothes_stack.pop()
    if rack_capacity >= current_clothes:
        rack_capacity -= current_clothes
    else:
        racks_number += 1
        rack_capacity = capacity
        rack_capacity -= current_clothes

print(racks_number)
