def in_range(index, string):
    is_in_range = True
    if not index <= len(string) - 1:
        is_in_range = False
    return is_in_range


string1, string2 = input().split()

result_sum = 0
max_lenght = max(len(string1), len(string2))

for index in range(max_lenght):
    if in_range(index, string1):
        str1 = ord(string1[index])
    else:
        str1 = 1
    if in_range(index, string2):
        str2 = ord(string2[index])
    else:
        str2 = 1
    result_sum += str1 * str2

print(result_sum)