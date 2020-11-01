# from math import ceil
empl_1 = int(input())
empl_2 = int(input())
empl_3 = int(input())
people = int(input())

hours = 0

while people > 0:
    hours += 1
    people -= empl_1 + empl_2 + empl_3
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

#
# people_per_hour = empl_1 + empl_2 + empl_3
# hours_working = ceil(people / people_per_hour)
# break_time = hours_working // 4
# total_time = hours_working + break_time
#
# print(f'Time needed: {total_time}h.')
