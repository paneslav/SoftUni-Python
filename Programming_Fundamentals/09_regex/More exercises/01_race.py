import re

participants_list = input().split(', ')

participants_dict = {}

for person in participants_list:
    participants_dict[person] = participants_dict.get(person, 0)

while True:
    total_distance = 0
    command = input()
    if command == 'end of race':
        break

    participant = ''.join(re.findall('[a-zA-Z]', command))

    distance = re.findall('\d', command)
    for digit in distance:
        total_distance += int(digit)

    if participant in participants_dict:
        participants_dict[participant] += total_distance

sort_by_points = sorted(participants_dict.items(), key=lambda item: -item[-1])

print(f"1st place: {sort_by_points[0][0]}")
print(f"2nd place: {sort_by_points[1][0]}")
print(f"3rd place: {sort_by_points[2][0]}")