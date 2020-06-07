# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit = float(input())
term = int(input())
yearly_int = float(input())

gross_amount = deposit + term * ((deposit * yearly_int/100) / 12)
print(gross_amount)
