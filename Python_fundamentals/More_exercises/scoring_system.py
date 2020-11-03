students = int(input())
lectures = int(input())
initial_bonus = int(input())
attendances = []
bonuses = []
max_bonus = 0
best_student_attendances = 0

if students > 0:
    for student_id in range(students):
        student_attendances = int(input())
        attendances.append(student_attendances)
        if student_attendances == 0:
            bonuses.append(0)
        else:
            bonus = student_attendances / lectures * (5 + initial_bonus)
            bonuses.append(bonus)

    max_bonus = max(bonuses)
    best_student_id = bonuses.index(max_bonus)
    best_student_attendances = attendances.pop(best_student_id)

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {best_student_attendances} lectures.')
