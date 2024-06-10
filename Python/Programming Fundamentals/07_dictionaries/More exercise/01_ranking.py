contests = {}
submissions = {}
contest_winner = 0
max_points = 0

while True:
    entry = input()
    if entry == 'end of contests':
        break

    entry = entry.split(':')
    contest = entry[0]
    password = entry[-1]
    contests[contest] = contests.get(contest, password)

while True:
    entry = input()
    if entry == 'end of submissions':
        break
    contest, password, username, points = entry.split('=>')

    if contest in contests and contests[contest] == password:
        submissions[username] = submissions.get(username, {})
        submissions[username][contest] = submissions[username].get(contest, int(points))
        if submissions[username][contest] < int(points):
            submissions[username][contest] = int(points)

for key in submissions:
    current_points = 0
    for nested_key, value in submissions[key].items():
        current_points += value
    if current_points > max_points:
        max_points = current_points
        contest_winner = key

sorted_tuples = sorted(submissions.items(), key=lambda item: item)
sorted_submissions = {k: v for k, v in sorted_tuples}

for key in sorted_submissions:
    values_to_sort = sorted_submissions[key]
    sorted_val_tuples = sorted(values_to_sort.items(), key=lambda item: -item[1])
    sorted_values = {k: v for k, v in sorted_val_tuples}
    sorted_submissions[key] = sorted_values

print(f"Best candidate is {contest_winner} with total {max_points} points.")
print("Ranking:")
for user in sorted_submissions:
    print(f"{user}")
    for value in sorted_submissions[user]:
        print(f"#  {value} -> {sorted_submissions[user][value]}")