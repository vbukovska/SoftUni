counter = 0
resources = {}

while True:
    command = input()
    counter += 1
    if command == 'stop':
        break
    if not counter % 2 == 0:
        key = command
    else:
        value = int(command)
        if key in resources:
            resources[key] += value
        else:
            resources[key] = value

[print(f"{key} -> {value}") for (key, value) in resources.items()]
