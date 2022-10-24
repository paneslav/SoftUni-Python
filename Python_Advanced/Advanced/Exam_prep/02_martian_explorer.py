def get_next_position(row, col, direction):
    if direction == 'down':
        row += 1
    elif direction == 'up':
        row -= 1
    elif direction == 'right':
        col += 1
    elif direction == 'left':
        col -= 1

    if row < 0:
        row = 5
    elif row >= size:
        row = 0

    if col < 0:
        col = 5
    elif col >= size:
        col = 0

    return row, col


board = []
size = 6

current_row, current_col = 0, 0

resources = {'W': 0, 'M': 0, 'C': 0}
acronyms = {'W': 'Water', 'M': 'Metal', 'C': 'Concrete'}

for row in range(size):
    line = input().split()

    if 'E' in line:
        col = line.index('E')
        current_row, current_col = row, col

    board.append(line)

commands = input().split(', ')

rover_is_broken = False

while commands:

    direction = commands.pop(0)

    next_row, next_col = get_next_position(current_row, current_col, direction)
    position = board[next_row][next_col]

    if position == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    if position in resources:
        resources[position] += 1
        print(f"{acronyms[position]} deposit found at ({next_row}, {next_col})")

    current_row, current_col = next_row, next_col

if all(item > 0 for item in resources.values()):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
