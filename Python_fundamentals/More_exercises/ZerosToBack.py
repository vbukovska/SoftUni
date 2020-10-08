# Solution 1:
# input_string = input().split(", ")
# string_to_num = [int(x) for x in input_string]
# removed_list = []
# while True:
#     try:
#         removed_list.append(string_to_num.pop(string_to_num.index(0)))
#     except:
#         break
# string_to_num.extend(removed_list)
#
# for num in range(len(string_to_num)):
#     if num < len(string_to_num) - 1:
#         print(string_to_num[num], end=', ')
#     else:
#         print(string_to_num[num])

# Solution 2:

input_string = input().split(", ")
string_to_num = [int(x) for x in input_string]
removed_list = []
while True:
    if 0 in string_to_num:
        removed_list.append(string_to_num.pop(string_to_num.index(0)))
    else:
        break
string_to_num.extend(removed_list)
print(string_to_num)
