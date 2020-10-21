version = input().split('.')
version_number = int(''.join(version))
new_version_number = version_number + 1
new_version = '.'.join(str(new_version_number))
print(new_version)


# def list_of_num(index, num, list_length):
#     return num * 10**(list_length - 1 - index)
# 
#
# version = [int(el) for el in input().split('.')]
# version_to_number = sum([list_of_num(index, version[index], len(version)) for index in range(len(version))])
# version_to_number += 1
# new_version = '.'.join(str(version_to_number))
# print(new_version)