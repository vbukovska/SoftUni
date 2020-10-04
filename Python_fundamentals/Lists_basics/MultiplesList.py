factor = int(input())
count = int(input())

multiples_list = []
num = 0

for i in range(1, count+1):
    num = factor * i
    multiples_list.append(num)

print(multiples_list)


# factor = int(input())
# count = int(input())
#
# multiples_list = []
# num = factor
#
# for i in range(count):
#     while not num % factor == 0:
#         num += 1
#     multiples_list.append(num)
#     num += 1
# print(multiples_list)