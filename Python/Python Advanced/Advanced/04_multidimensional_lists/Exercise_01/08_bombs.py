def check_neighbours(matrix, x, y):
    possible_neighbours = [
        [x - 1, y - 1],
        [x - 1, y],
        [x - 1, y + 1],
        [x, y - 1],
        [x, y + 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1]
    ]

    result = []

    for row, col in possible_neighbours:
        if 0 <= row < len(matrix) and 0 <= col < len(matrix) and matrix[row][col] > 0:
            result.append([row, col])

    return result


size = int(input())

matrix = [[int(x) for x in input().split()] for row in range(size)]
bombs = input().split()
alive_cells = 0
sum = 0

for item in bombs:
    x, y = [int(x) for x in item.split(',')]
    bomb = matrix[x][y]

    if bomb <= 0:
        continue

    matrix[x][y] = 0

    children = check_neighbours(matrix, x, y)

    for child_row, child_col in children:
        matrix[child_row][child_col] -= bomb


for row in matrix:
    for i in row:
        if i > 0:
            alive_cells += 1
            sum += i


print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")

for row in matrix:
    print(*row, sep=' ')
