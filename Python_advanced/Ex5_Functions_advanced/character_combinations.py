from collections import deque


# def char_combinations(string, combos=[]):
#     que_combo = deque([el for el in string])
#     stack_combo = [el for el in string]
#     char_forward = que_combo.popleft()
#     combos.append(char_forward)
#     char_combinations()
#     char_backwards = stack_combo.pop()


def char_combinations(string, step=0):
    if step == len(string):
        print(''.join(string))
        return

    for i in range(step, len(string)):
        string[step], string[i] = string[i], string[step]
        char_combinations(string, step + 1)
        string[step], string[i] = string[i], string[step]


string = [el for el in input()]
char_combinations(string)