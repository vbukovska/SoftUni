import re
data = input()

pattern = r"(^|(?<=\s))[a-z0-9]+[._-]?[a-z]+@([a-z]+-?[a-z]+\.)+[a-z]+\b"

emails = re.finditer(pattern, data)
emails = [email.group() for email in emails]

print('\n'.join(emails))