cheaters = []
submissions = {}
results = {}

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
        if username not in submissions:
            submissions[username] = {}
        if language not in submissions[username]:
            submissions[username][language] = []
        submissions[username][language].append(points)

sorted_submissions = dict(sorted(submissions.items(), key=lambda x: (-max(x[1].values()), x[0])))

print('Results:')
for user in sorted_submissions:
    if user not in cheaters:
        max_result = max(sorted_submissions[user].values())[0]
        print(f'{user} | {max_result}')

for submits in sorted_submissions.values():
    for technology, result_points in submits.items():
        if technology not in results:
            results[technology] = []
        results[technology].extend(result_points)

sorted_results = sorted(results.items(), key=lambda x: (-len(x[1]), x[0]))

print('Submissions:')
for technology, submits in sorted_results:
    print(f'{technology} - {len(submits)}')
