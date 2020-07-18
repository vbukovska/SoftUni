name = input()
elder_tickets = int(input())
child_tickets = int(input())
elder_ticket_price = float(input())
fee = float(input())

elder_fin_price = elder_ticket_price + fee
child_fin_price = elder_ticket_price * 0.3 + fee

total = elder_tickets * elder_fin_price + child_tickets * child_fin_price
profit = total * 0.2

print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')
