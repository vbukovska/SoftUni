courses = {}

while True:
    command = input()
    if 'end' in command:
        break
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

ordered_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for course in ordered_courses:
    print(f"{course}: {len(ordered_courses[course])}")
    ordered_students = list(sorted(x for x in courses[course]))
    [print(f'-- {student}') for student in ordered_students]
