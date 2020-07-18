pen = int(input())
marker = int(input())
detergent = float(input())
discount = int(input())

bill = pen * 5.8 + marker * 7.2 + detergent * 1.2
total = bill - bill * discount / 100
print(f'{total:.3f}')
