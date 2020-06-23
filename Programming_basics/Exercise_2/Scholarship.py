import math
income = float(input())
grade = float(input())
min_salary = float(input())

social_scholarship = 0
grade_scholarship = 0

if income < min_salary and grade > 4.5:
    social_scholarship = math.floor(min_salary * 0.35)
if grade >= 5.5:
    grade_scholarship = math.floor(grade * 25)

sum_scholarship = social_scholarship + grade_scholarship

if sum_scholarship == 0:
    print(f'You cannot get a scholarship!')
elif sum_scholarship == social_scholarship or social_scholarship > grade_scholarship:
    print(f'You get a Social scholarship {social_scholarship} BGN')
else:
    print(f'You get a scholarship for excellent results {grade_scholarship} BGN')


# sum_scholarship == grade_scholarship or grade_scholarship >= social_scholaship
