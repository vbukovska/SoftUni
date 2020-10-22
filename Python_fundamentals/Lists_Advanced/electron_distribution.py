electrons = int(input())
shells = []
index = 1
while electrons > 0:
    curr_shell = 2*index**2
    if curr_shell < electrons:
        shells.append(curr_shell)
        electrons -= curr_shell
    else:
        shells.append(electrons)
        electrons = 0
    index += 1
print(shells)
