first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

students = int(input())

people_per_hour = first_employee + second_employee + third_employee
time = 0

if students > 0:
    while students > 0:
        students -= people_per_hour
        time += 1
        if time % 4 == 0:
            time += 1
print(f'Time needed: {time}h.')