number_students = int(input())

students_grades = {}

for _ in range(number_students):
    student = input()
    grade = float(input())
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

students_grades = dict(filter(lambda x: sum(x[1])/len(x[1]) >= 4.50 ,students_grades.items()))
ordered_students = dict(sorted(students_grades.items(), key=lambda x: -sum(x[1])/len(x[1])))
for student in ordered_students:
    avg_grade = sum(ordered_students[student])/len(ordered_students[student])
    print(f'{student} -> {avg_grade:.2f}')

# [print(f"{student} -> {sum(ordered_students[student])/len(ordered_students[student])}") for student in ordered_students]

