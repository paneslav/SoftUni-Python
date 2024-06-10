to_do_list = []
sorted_list = []

while True:

    command = input().split('-')

    if command[0] == 'End':
        break

    priority = int(command[0])
    task = command[1]

    to_do_list.append((priority, task))
    sorted_list = [x[1] for x in sorted(to_do_list)]

print(sorted_list)