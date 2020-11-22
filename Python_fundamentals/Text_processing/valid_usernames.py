def is_valid_characters(username):
    is_valid = True
    for character in username:
        if not(character.isalpha() or character.isnumeric() or character in ('-', '_')):
            is_valid = False
    return is_valid


user_names = input().split(', ')

valid_usernames = []

for username in user_names:
    if 3 <= len(username) <= 16 and is_valid_characters(username):
        valid_usernames.append(username)

print('\n'.join(valid_usernames))

