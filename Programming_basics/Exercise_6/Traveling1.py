
while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    while budget > 0:
        budget -= float(input())
    print(f'Going to {destination}!')
