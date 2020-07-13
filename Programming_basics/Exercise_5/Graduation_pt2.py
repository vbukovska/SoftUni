student = input()
curr_grade = 1
low_grade = 0
sum_grades = 0
while curr_grade <= 12:
    grade = float(input())
    if grade < 4:
        low_grade += 1
        if low_grade > 1:
            print(f'{student} has been excluded at {curr_grade} grade')
            break
        continue
    sum_grades += grade
    curr_grade += 1

if low_grade <= 1:
    avg_grade = sum_grades / (curr_grade-1)
    print(f'{student} graduated. Average grade: {avg_grade:.2f}')
