words = input().split()

[print(x) for x in words if len(x) % 2 == 0]