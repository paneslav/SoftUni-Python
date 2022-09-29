matrix = []

rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    matrix.append([x for x in input()])

directions = list(input())

player_x = int
player_y = int

# find P
for row in range(rows):
    if 'P' in matrix[row]:
        player_x = row
        player_y = matrix[row].index('P')

print(player_x, player_y)