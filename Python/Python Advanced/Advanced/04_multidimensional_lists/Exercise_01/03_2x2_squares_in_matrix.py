rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for row in range(rows)]

total_identical = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]

        if top_left == top_right == bottom_left == bottom_right:
            total_identical += 1

print(total_identical)