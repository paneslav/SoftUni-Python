size = int(input())

matrix = [[int(x) for x in input().split()] for i in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-1 - row])

sum_primary = sum(primary_diagonal)
sum_secondary = sum(secondary_diagonal)
difference = abs(sum_primary - sum_secondary)

print(difference)

