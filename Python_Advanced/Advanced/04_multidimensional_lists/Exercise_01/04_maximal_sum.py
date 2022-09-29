import sys

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

biggest_submatrix = []
biggest_sum = -sys.maxsize

for row in range(rows - 2):
    for col in range(cols - 2):
        current_submatrix = []
        current_sum = int

        for i in range(3):
            current_submatrix.append(matrix[row + i][col: 3 + col])

        current_sum = sum(current_submatrix[0]) + sum(current_submatrix[1]) + sum(current_submatrix[-1])
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_submatrix = current_submatrix

print(f"Sum = {biggest_sum}")
for row in range(3):
    print(*biggest_submatrix[row])
