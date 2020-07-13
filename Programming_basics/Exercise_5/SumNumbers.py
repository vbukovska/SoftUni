number_sum = int(input())

number = int(input())
total = number

while total < number_sum:
    number = int(input())
    total += number

print(total)