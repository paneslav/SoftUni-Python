import math

numbers = list(map(int, input().split(', ')))

groups_count = math.ceil(max(numbers) / 10)

groups_list = []

counter = 10
starting_counter = 0

for i in range(1, groups_count + 1):
    for number in numbers:
        if starting_counter < number <= counter:
            groups_list.append(number)

    print(f"Group of {counter}'s: {groups_list}")
    counter += 10
    starting_counter += 10
    groups_list = []