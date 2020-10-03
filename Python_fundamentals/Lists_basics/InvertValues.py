string = input()

list_of_string = string.split(' ')
reverse_list = []
for i in range(len(list_of_string)):
    reverse_list.append(int(list_of_string[i]) * -1)

print(reverse_list)

