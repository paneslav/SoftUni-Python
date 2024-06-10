stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    action = command[0]

    if action == 'Add Stop':
        place_to_insert = int(command[1])
        stop = command[-1]

        if place_to_insert < len(stops):
            stops = stops[:place_to_insert] + stop + stops[place_to_insert:]

    elif action == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[-1])

        if start_index < len(stops) and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+ 1:]

    elif action == 'Switch':
        old_string = command[1]
        new_string = command[-1]

        if old_string in stops:
            stops = stops.replace(old_string.strip(), new_string.strip())

    print(stops)
