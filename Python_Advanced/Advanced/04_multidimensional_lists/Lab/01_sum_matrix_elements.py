rows, cols = [int(x) for x in input().split(", ")]
matrix = []

sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    for col in range(cols):
        sum += matrix[row][col]

print(sum)
print(matrix)