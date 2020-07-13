import sys

command = input()

max_number = -sys.maxsize

while command != 'Stop':

    number = int(command)

    if max_number < number:
        max_number = number

    command = input()
print(max_number)
