low_grades_allowed = int(input())

num_exercises = 0
tot_score = 0
low_grades = 0


while low_grades < low_grades_allowed:
    command = input()
    if command == 'Enough':
        print(f'Average score: {tot_score / num_exercises:.2f} ')
        print(f'Number of problems: {num_exercises}')
        print(f'Last problem: {curr_exercise}')
        break
    curr_exercise = command
    num_exercises += 1
    grade = int(input())
    tot_score += grade
    if grade <= 4:
        low_grades += 1


if low_grades >= low_grades_allowed:
    print(f'You need a break, {low_grades} poor grades.')
