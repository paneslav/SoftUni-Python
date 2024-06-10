import sys

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for row in range(rows)]

biggest_submatrix = []
biggest_sum = -sys.maxsize

for row in range(rows - 1):
    for col in range(cols - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]
        current_submatrix = [top_left, top_right, bottom_left, bottom_right]
        current_sum = sum(current_submatrix)

        if current_sum > biggest_sum:
            biggest_submatrix = current_submatrix
            biggest_sum = current_sum

print(f"{biggest_submatrix[0]} {biggest_submatrix[1]}")
print(f"{biggest_submatrix[2]} {biggest_submatrix[3]}")
print(biggest_sum)