hour = int(input())
weekday = input()

if (weekday == 'Monday' or weekday == 'Tuesday' or weekday == 'Wednesday' or weekday == 'Thursday' or weekday == 'Friday' or weekday == 'Saturday') and 10 <= hour <= 18:
    print('open')
else:
    print('closed')
