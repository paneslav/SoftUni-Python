def get_next_position(row, col):
    if direction == 'up':
        row -= 1
        if row < 0: row = ROWS - 1
    elif direction == 'down':
        row += 1
        if row >= ROWS: row = 0
    elif direction == 'right':
        col += 1
        if col >= COLS: col = 0
    elif direction == 'left':
        col -= 1
        if col < 0: col = COLS - 1

    return row, col


board = []
collected = 0
total_items_on_field = 0
collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}

end_program = False

ROWS, COLS = [int(x) for x in input().split(', ')]

current_row, current_col = 0, 0

for row in range(ROWS):
    line = input().split()
    for col in range(COLS):
        if line[col] in 'DGC':
            total_items_on_field += 1
        if line[col] == 'Y':
            current_row, current_col = row, col
    board.append(line)

while True:
    command = input()
    if command == 'End':
        break

    direction, steps = command.split('-')

    for i in range(int(steps)):
        board[current_row][current_col] = 'x'
        next_row, next_col = get_next_position(current_row, current_col)
        position = board[next_row][next_col]

        if position == 'D':
            collected_items['Christmas decorations'] += 1
            collected += 1
        elif position == 'G':
            collected_items['Gifts'] += 1
            collected += 1
        elif position == 'C':
            collected_items['Cookies'] += 1
            collected += 1

        current_row, current_col = next_row, next_col
        board[current_row][current_col] = 'Y'

        if collected == total_items_on_field:  # check whether all items are collected and end the program
            end_program = True
            break

    if end_program:
        break

if collected == total_items_on_field:
    print(f"Merry Christmas!")

print("You've collected:")
for key, value in collected_items.items():
    print(f"- {value} {key}")

for line in board:
    print(*line, sep=' ')
