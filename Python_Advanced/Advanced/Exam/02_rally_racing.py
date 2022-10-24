def get_next_position(car_row, car_col, direction):
    if direction == 'up':
        car_row -= 1
    elif direction == 'down':
        car_row += 1
    elif direction == 'right':
        car_col += 1
    elif direction == 'left':
        car_col -= 1
    return car_row, car_col


track_size = int(input())
tracked_car = input()

car_row, car_col = 0, 0
track = []
tunnel = []

has_won = False

km_passed = 0

# create board
for row in range(track_size):
    current_row = input().split()
    if 'T' in current_row:
        tunnel.append([row, current_row.index('T')])

    track.append(current_row)

# start game
while True:
    direction = input()
    if direction == 'End':
        track[car_row][car_col] = 'C'
        break

    next_row, next_col = get_next_position(car_row, car_col, direction)
    next_position = track[next_row][next_col]

    if next_position == 'F':
        has_won = True
        track[next_row][next_col] = 'C'
        km_passed += 10
        break
    elif next_position == 'T':
        km_passed += 30
        entry = tunnel.index([next_row, next_col])
        entry_row, entry_col = tunnel.pop(entry)
        dest_row, dest_col = tunnel[0]

        track[entry_row][entry_col] = '.'
        track[dest_row][dest_col] = '.'

        car_row, car_col = dest_row, dest_col
        continue

    km_passed += 10
    car_row, car_col = next_row, next_col

if has_won:
    print(f"Racing car {tracked_car} finished the stage!")
else:
    print(f"Racing car {tracked_car} DNF.")

print(f"Distance covered {km_passed} km.")
for row in track:
    print(f"{''.join(row)}")
