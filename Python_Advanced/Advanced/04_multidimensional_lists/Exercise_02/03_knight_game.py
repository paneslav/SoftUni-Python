def get_moves(row, col, matrix):
    poss_moves = [
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row + 1, col + 2],
        [row + 1, col - 2],
        [row + 2, col - 1],
        [row + 2, col + 1]

    ]

    attacked_knights_count = 0

    for r, c in poss_moves:
        if 0 <= r < size and 0 <= c < size and matrix[r][c] == 'K':
            attacked_knights_count += 1

    return attacked_knights_count


size = int(input())
matrix = []

removed_knights = 0

for row in range(size):
    matrix.append([x for x in input()])

while True:
    number_of_attacked_knights = 0
    winner_row = 0
    winner_col = 0

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == '0':
                continue

            enemies = get_moves(row, col, matrix)

            if enemies > number_of_attacked_knights:
                number_of_attacked_knights = enemies
                winner_row = row
                winner_col = col

    if number_of_attacked_knights:
        matrix[winner_row][winner_col] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)