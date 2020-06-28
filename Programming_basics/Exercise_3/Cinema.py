type_screening = input()
rows = int(input())
columns = int(input())


capacity = rows * columns
ticket_price = 0

if type_screening == 'Premiere':
    ticket_price = 12
elif type_screening == 'Normal':
    ticket_price = 7.5
else:
    ticket_price = 5

print(f'{capacity * ticket_price:.2f} leva')

