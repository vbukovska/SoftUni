count_standard = 0
count_kid = 0
count_student = 0
counter = 0
tot_standard = 0
tot_student = 0
tot_kid = 0

movie = input()
while True:
    if movie == 'Finish':
        break
    free_sits = int(input())
    while True:
        type_sits = input()
        if type_sits == 'End':
            break
        else:
            counter += 1
        if type_sits == 'standard':
            count_standard += 1
        elif type_sits == 'kid':
            count_kid += 1
        else:
            count_student += 1
        if free_sits == count_student + count_kid + count_standard:
            break
    print(f'{movie} - {((count_student + count_kid + count_standard) / free_sits) * 100:.2f}% full.')
    movie = input()
    tot_kid += count_kid
    tot_student += count_student
    tot_standard += count_standard
    count_standard = 0
    count_kid = 0
    count_student = 0
print(f'Total tickets: {counter}')
print(f'{(tot_student / counter) * 100:.2f}% student tickets.')
print(f'{(tot_standard / counter) * 100:.2f}% standard tickets.')
print(f'{(tot_kid / counter) * 100:.2f}% kids tickets.')

