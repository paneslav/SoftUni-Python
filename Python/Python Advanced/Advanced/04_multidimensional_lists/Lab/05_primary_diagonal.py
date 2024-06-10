size = int(input())

matrix = [[int(x) for x in input().split()] for row in range(size)]

sum = 0
for row in range(size):
    sum += matrix[row][row]

print(sum)
