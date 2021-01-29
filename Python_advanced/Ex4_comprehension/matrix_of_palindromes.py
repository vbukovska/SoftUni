rows, cols = [int(n) for n in input().split()]
row_symbols = [ord('a') + i for i in range(rows)]
result = [[chr(row_symbols[r]) + chr(row_symbols[r] + c) + chr(row_symbols[r]) for c in range(cols)] for r in range(rows)]
[print(' '.join(row)) for row in result]