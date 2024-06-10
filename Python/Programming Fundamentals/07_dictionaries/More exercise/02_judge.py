exams_info = {}
individual_ranking = {}

while True:
    command = input().split(' -> ')

    if command[0] == 'no more time':
        break

    username = command[0]
    contest = command[1]
    points = int(command[-1])

    exams_info[contest] = exams_info.get(contest, {})
    exams_info[contest][username] = exams_info[contest].get(username, points)
    individual_ranking[username] = individual_ranking.get(username, 0)
    if exams_info[contest][username] < points:
        exams_info[contest][username] = points
        individual_ranking[username] += points - individual_ranking[username]
        continue
    individual_ranking[username] += points


for exam in exams_info:
    counter = 1
    print(f"{exam}: {len(exams_info[exam])} participants")
    for user in exams_info[exam]:
        print(f"{counter}. {user} <::> {exams_info[exam][user]}")
        counter += 1

print("Individual standings:")

another_counter = 1
for item in sorted(individual_ranking.items(), key=lambda x: -x[1]):
    print(f"{another_counter}. {item[0]} -> {item[1]}")
    another_counter += 1
