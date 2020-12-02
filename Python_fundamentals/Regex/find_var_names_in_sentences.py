import re

data = input()

pattern = r"(^_|(?<= _))([A-Za-z0-9]+)($|(?=\s))"

variables = re.finditer(pattern, data)
variables = [var.group() for var in variables]

print(','.join(variables))