rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for row in range(rows)]
# for row in range(rows):
#     matrix.append([int(x) for x in input().split()])


for col in range(cols):
    sum = 0
    for row in range(rows):
        sum += matrix[row][col]
    print(sum)