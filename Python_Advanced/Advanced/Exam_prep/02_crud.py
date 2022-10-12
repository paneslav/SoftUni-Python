def get_next_position(direction, latest_row, latest_col):
    if direction == 'up':
        return latest_row - 1, latest_col
    elif direction == 'down':
        return latest_row + 1, latest_col
    elif direction == 'left':
        return latest_row, latest_col - 1
    elif direction == 'right':
        return latest_row, latest_col + 1


matrix = []

empty_block = '.'

for row in range(6):
    matrix.append([x for x in input().split()])

latest_row, latest_col = [int(x) for x in input() if x.isdigit()]

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    action = command[0]
    direction = command[1]

    next_row, next_col = get_next_position(direction, latest_row, latest_col)

    if action == 'Create':
        new_value = command[-1]

        if matrix[next_row][next_col] == empty_block:
            matrix[next_row][next_col] = new_value

    elif action == 'Update':
        new_value = command[-1]

        if matrix[next_row][next_col].isdigit() or matrix[next_row][next_col].isalpha():
            matrix[next_row][next_col] = new_value

    elif action == 'Delete':
        if matrix[next_row][next_col] != empty_block:
            matrix[next_row][next_col] = empty_block

    elif action == 'Read':
        if matrix[next_row][next_col].isdigit() or matrix[next_row][next_col].isalpha():
            print(matrix[next_row][next_col])

    latest_row, latest_col = next_row, next_col


for row in matrix:
    print(*row, sep=' ')
