cheaters = []
user_submissions = {}
language_submissions = {}


while True:
    command_line = input()
    if command_line == 'exam finished':
        break
    if 'banned' in command_line:
        username, command = command_line.split('-')
        cheaters.append(username)
    else:
        username, language, points = command_line.split('-')
        points = int(points)
        if username not in user_submissions:
            user_submissions[username] = []
        user_submissions[username].append(points)
        if language not in language_submissions:
            language_submissions[language] = []
        language_submissions[language].append(points)

sorted_users = dict(sorted(user_submissions.items(), key=lambda x: (-max(x[1]), x[0])))
sorted_languages = dict(sorted(language_submissions.items(), key=lambda x: (-len(x[1]), x[0])))

print('Results:')
for user in sorted_users:
    if user not in cheaters:
        max_result = max(sorted_users[user])
        print(f'{user} | {max_result}')

print('Submissions:')
for technology, submits in sorted_languages.items():
    print(f'{technology} - {len(submits)}')
