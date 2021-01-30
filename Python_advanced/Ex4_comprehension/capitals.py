countries = input().split(', ')
cities = input(). split(', ')
zipped = zip(countries, cities)

result = {x: y for (x, y) in zipped}
[print(f'{key} -> {value}') for (key, value) in result.items()]