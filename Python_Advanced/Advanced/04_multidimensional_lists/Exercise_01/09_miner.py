size = int(input())

movements = [x for x in input().split()]
matrix = []

total_coal = 0
coal = 0

for row in range(size):  # create matrix
    matrix.append([x for x in input().split()])

for row in matrix:  # find total coal
    total_coal += row.count('c')

starting_row = int
starting_col = int
next_spot = ''

game_over = False

for row in matrix:
    if 's' in row:
        starting_row = matrix.index(row)
        starting_col = row.index('s')

while movements and coal != total_coal:
    direction = movements.pop(0)

    if direction == 'up' and 0 <= starting_row - 1 < size:
        next_spot = matrix[starting_row - 1][starting_col]
        matrix[starting_row][starting_col] = '*'
        starting_row = starting_row - 1

    elif direction == 'down' and 0 <= starting_row + 1 < size:
        next_spot = matrix[starting_row + 1][starting_col]
        matrix[starting_row][starting_col] = '*'
        starting_row = starting_row + 1

    elif direction == 'right' and 0 <= starting_col + 1 < size:
        next_spot = matrix[starting_row][starting_col + 1]
        matrix[starting_row][starting_col] = '*'
        starting_col = starting_col + 1

    elif direction == 'left' and 0 <= starting_col - 1 < size:
        next_spot = matrix[starting_row][starting_col - 1]
        matrix[starting_row][starting_col] = '*'
        starting_col = starting_col - 1

    if next_spot == 'c':
        coal += 1
    elif next_spot == 'e':
        game_over = True

    if game_over:
        print(f"Game over! ({starting_row}, {starting_col})")
        break

if not game_over:
    if total_coal == coal:
        print(f"You collected all coal! ({starting_row}, {starting_col})")
    else:
        print(f"{total_coal - coal} pieces of coal left. ({starting_row}, {starting_col})")