exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
minutes_difference = 0

if arrival_hour == exam_hour:
    if arrival_minute > exam_minute:
        minutes_difference = arrival_minute - exam_minute
        print('Late')
        print(f'{minutes_difference} minutes after the start')
    elif exam_minute - 30 <= arrival_minute < exam_minute:
        minutes_difference = exam_minute - arrival_minute
        print('On time')
        print(f'{minutes_difference} minutes before the start')
    elif arrival_minute == exam_minute:
        print('On time')
    else:
        minutes_difference = exam_minute - arrival_minute
        print('Early')
        print(f'{minutes_difference} minutes before the start')
elif arrival_hour < exam_hour:
    minutes_difference = (exam_hour - arrival_hour)*60 + exam_minute - arrival_minute
    if minutes_difference <= 30:
        print('On time')
        print(f'{minutes_difference} minutes before the start')
    elif minutes_difference < 60:
        print('Early')
        print(f'{minutes_difference} minutes before the start')
    else:
        print('Early')
        if minutes_difference % 60 <= 9:
            print(f'{minutes_difference // 60}:0{minutes_difference % 60} hours before the start')
        else:
            print(f'{minutes_difference // 60}:{minutes_difference % 60} hours before the start')
elif arrival_hour > exam_hour:
    print('Late')
    minutes_difference = (arrival_hour - exam_hour)*60 + arrival_minute - exam_minute
    if minutes_difference // 60 == 0:
        print(f'{minutes_difference} minutes after the start')
    else:
        if minutes_difference % 60 <= 9:
            print(f'{minutes_difference // 60}:0{minutes_difference % 60} hours after the start')
        else:
            print(f'{minutes_difference // 60}:{minutes_difference % 60} hours after the start')