goal = 10000

tot_steps = 0
command = input()
is_goal_reached = False
while command != 'Going home':
    steps = int(command)
    tot_steps += steps
    if tot_steps >= goal:
        is_goal_reached = True
        break
    command = input()

if is_goal_reached:
    print('Goal reached! Good job!')
    print(f'{tot_steps - goal} steps over the goal!')
else:
    tot_steps += int(input())
    if tot_steps >= goal:
        print('Goal reached! Good job!')
        print(f'{tot_steps - goal} steps over the goal!')
    else:
        print(f'{goal - tot_steps} more steps to reach goal.')
