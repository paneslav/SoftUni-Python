from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = deque(list(input()))
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        left = snake.popleft()
        matrix[row].append(left)
        snake.append(left)

for i in range(rows):
    if i % 2 == 0:
        print(''.join(matrix[i]))
    else:
        print(''.join(reversed(matrix[i])))