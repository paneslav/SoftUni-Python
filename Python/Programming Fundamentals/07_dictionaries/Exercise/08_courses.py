courses_data = {}

while True:
    command = input().split(' : ')
    if command[0] == 'end':
        break

    course = command[0]
    name = command[1]

    if course not in courses_data:
        courses_data[course] = []
    courses_data[course].append(name)

for course in courses_data:
    data_to_print = [f'-- {name}' for name in courses_data[course]]
    print(f"{course}: {len(courses_data[course])}")
    print('\n'.join(data_to_print))
    