bitcoin = int(input())
jan = float(input())
comm = float(input())

total_eur = (bitcoin * 1168 + jan * 0.15 * 1.76) / 1.95
total = total_eur - total_eur*(comm/100)
print(f'{total:.2f}')

