numbers = input().split()
num_to_remove = int(input())
integer_numbers = [int(x) for x in numbers]

for i in range(num_to_remove):
    integer_numbers.remove(min(integer_numbers))

print(integer_numbers)