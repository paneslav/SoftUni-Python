def is_outside(row, col):
    if row < 0 or row >= size or col < 0 or col >= size:
        return True


size = int(input())

matrix = []


for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break

    operation = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if is_outside(int(row), int(col)):
        print(f"Invalid coordinates")
    else:
        if operation == 'Add':
            matrix[row][col] += int(value)
        else:
            matrix[row][col] -= int(value)

[print(*x) for x in matrix]