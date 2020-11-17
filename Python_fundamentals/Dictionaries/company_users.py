companies = {}

while True:
    command = input()
    if 'End' in command:
        break
    company, employee = command.split(' -> ')
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

ordered_companies = dict(sorted(companies.items(), key=lambda x: x[0]))
for curr_company in ordered_companies:
    print(curr_company)
    [print(f'-- {comp}') for comp in ordered_companies[curr_company]]