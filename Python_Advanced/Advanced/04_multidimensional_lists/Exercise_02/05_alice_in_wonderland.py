directions = {
    'up': lambda r, c: [r - 1, c],
    'down': lambda r, c: [r + 1, c],
    'left': lambda r, c: [r, c - 1],
    'right': lambda r, c: [r, c + 1],
}

size = int(input())
matrix = []

starting_row = 0
starting_col = 0

collected_tea = 0

game_over = False

for row in range(size):
    current_row = input().split()
    for col in range(size):
        if current_row[col] == 'A':
            starting_row = row
            starting_col = col
    matrix.append(current_row)

while collected_tea < 10:
    go = input()
    matrix[starting_row][starting_col] = '*'
    next_row, next_col = directions[go](starting_row, starting_col)

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        break
    elif matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        game_over = True
    elif matrix[next_row][next_col].isdigit():
        collected_tea += int(matrix[next_row][next_col])
        matrix[next_row][next_col] = '*'

    if game_over:
        break

    starting_row = next_row
    starting_col = next_col

if collected_tea >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()
