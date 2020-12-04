import re

string = input()
pattern = r"\b(www\.{1}[a-z0-9A-Z-]+)(\.{1}[a-z]+)+\b"
while string:
    match = re.finditer(pattern, string)
    match = [m.group(0) for m in match]
    if match:
        print(*match)
    string = input()
