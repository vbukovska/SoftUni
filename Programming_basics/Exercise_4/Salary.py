n = int(input())
salary = float(input())
website = ''
for i in range(n):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <= 0:
        exit(print('You have lost your salary.'))


print(f'{int(salary)}')
