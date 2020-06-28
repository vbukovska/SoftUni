age = float(input())
gender = str(input())

if gender == 'f':
    if age < 16:
        print('Miss')
    else:
        print('Ms.')
else:
    if age < 16:
        print('Master')
    else:
        print('Mr.')
