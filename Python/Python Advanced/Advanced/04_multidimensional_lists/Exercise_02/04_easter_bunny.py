def check_up(bunny_row, bunny_col, matrix):
    result = ['up', 0]

    while bunny_row >= 0:
        if matrix[bunny_row][bunny_col].isdigit():
            result[-1] += int(matrix[bunny_row][bunny_col])
            result.insert(-1, [bunny_row, bunny_col])
        elif matrix[bunny_row][bunny_col] == 'X':
            break
        bunny_row -= 1

    return result


def check_down(bunny_row, bunny_col, matrix):
    result = ['down', 0]

    while bunny_row < size:
        if matrix[bunny_row][bunny_col].isdigit():
            result[-1] += int(matrix[bunny_row][bunny_col])
            result.insert(-1, [bunny_row, bunny_col])
        elif matrix[bunny_row][bunny_col] == 'X':
            break

        bunny_row += 1

    return result

def check_left(bunny_row, bunny_col, matrix):
    result = ['left', 0]

    while bunny_col >= 0:
        if matrix[bunny_row][bunny_col].isdigit():
            result[-1] += int(matrix[bunny_row][bunny_col])
            result.insert(-1, [bunny_row, bunny_col])
        elif matrix[bunny_row][bunny_col] == 'X':
            break

        bunny_col -= 1

    return result


def check_right(bunny_row, bunny_col, matrix):
    result = ['right', 0]

    while bunny_col < size:
        if matrix[bunny_row][bunny_col].isdigit():
            result[-1] += int(matrix[bunny_row][bunny_col])
            result.insert(-1, [bunny_row, bunny_col])
        elif matrix[bunny_row][bunny_col] == 'X':
            break

        bunny_col += 1

    return result


size = int(input())
matrix = []

bunny_row = 0
bunny_col = 0

biggest_egg = float('-inf')
winner = []

for row in range(size):
    matrix.append([x for x in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'B':
            bunny_row = row
            bunny_col = col


points_up = check_up(bunny_row, bunny_col, matrix)
points_down = check_down(bunny_row, bunny_col, matrix)
points_left = check_left(bunny_row, bunny_col, matrix)
points_right = check_right(bunny_row, bunny_col, matrix)

all_together = [points_up, points_down, points_left, points_right]

for item in all_together:
    if item[-1] > biggest_egg and len(item) > 2:
        winner = item
        biggest_egg = item[-1]


[print(x) for x in winner]

