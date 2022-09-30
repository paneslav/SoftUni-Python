def is_outside(row, col):
    return row < 0 or row >= 5 or col < 0 or col >= 5 or matrix[row][col] != '.'


directions = {
    'up': lambda r, c, s: [r - s, c],
    'down': lambda r, c, s: [r + s, c],
    'right': lambda r, c, s: [r, c + s],
    'left': lambda r, c, s: [r, c - s],
}

matrix = []

start_row = 0
start_col = 0
targets_count = 0

killed_targets = []

for row in range(5):
    current_row = input().split()
    matrix.append(current_row)

    if 'A' in current_row:
        start_row, start_col = row, current_row.index('A')
    targets_count += current_row.count('x')

matrix[start_row][start_col] = '.'

n = int(input())

for i in range(n):
    if targets_count == 0:
        break

    command = input().split()

    action = command[0]
    direction = command[1]

    if action == 'move':
        steps_count = int(command[-1])
        next_row, next_col = directions[direction](start_row, start_col, steps_count)

        if is_outside(next_row, next_col):
            continue

        start_row, start_col = next_row, next_col
    elif action == 'shoot':
        bullet_row, bullet_col = start_row, start_col
        while True:
            next_row, next_col = directions[direction](bullet_row, bullet_col, 1)

            if next_row < 0 or next_row >= 5 or next_col < 0 or next_col >= 5:
                break

            if matrix[next_row][next_col] == 'x':
                matrix[next_row][next_col] = '.'
                targets_count -= 1
                killed_targets.append([next_row, next_col])
                break

            bullet_row, bullet_col = next_row, next_col

if targets_count == 0:
    print(f"Training completed! All {len(killed_targets)} targets hit.")
else:
    print(f"Training not completed! {targets_count} targets left.")

[print(x) for x in killed_targets]
