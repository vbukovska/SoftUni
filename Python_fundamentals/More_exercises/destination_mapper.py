import re

string = input()

pattern = r"(=|/)(?P<destination>[A-Z][A-Za-z]{2,})\1"

destinations = re.finditer(pattern, string)

destinations = [destination.groupdict() for destination in destinations]

travel_points = 0
for destination in destinations:
    travel_points += len(destination['destination'])

print(f"Destinations: {', '.join([curr_destination['destination'] for curr_destination in destinations])}")
print(f"Travel points: {travel_points}")
