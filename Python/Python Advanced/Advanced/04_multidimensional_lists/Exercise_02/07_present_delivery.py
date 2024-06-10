def get_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


def is_outside(row, col):
    if row < 0 or row >= size or col < 0 or col >= size:
        return True


def presents_for_everyone(row, col):
    mooves = [
        [row - 1, col],
        [row + 1, col],
        [row, col + 1],
        [row, col - 1],
    ]
    return mooves


presents_count = int(input())
size = int(input())
matrix = []

santa_row = 0
santa_col = 0
total_nice_kids = 0
nice_kids_with_presents = 0

for row in range(size):
    matrix_row = input().split()
    for col in range(size):
        if matrix_row[col] == 'S':
            santa_row = row
            santa_col = col
        elif matrix_row[col] == 'V':
            total_nice_kids += 1
    matrix.append(matrix_row)

while presents_count > 0:
    direction = input()
    if direction == 'Christmas morning':
        break

    next_row, next_col = get_next_position(santa_row, santa_col, direction)

    if is_outside(next_row, next_col):
        continue

    matrix[santa_row][santa_col] = '-'

    if matrix[next_row][next_col] == 'V':
        presents_count -= 1
        nice_kids_with_presents += 1
    elif matrix[next_row][next_col] == 'C':
        mooves = presents_for_everyone(next_row, next_col)
        for cookie_row, cookie_col in mooves:
            if presents_count == 0:
                break
            if matrix[cookie_row][cookie_col] == 'V':
                presents_count -= 1
                nice_kids_with_presents += 1
            elif matrix[cookie_row][cookie_col] == 'X':
                presents_count -= 1

            matrix[cookie_row][cookie_col] = '-'

    matrix[next_row][next_col] = 'S'
    santa_row, santa_col = next_row, next_col

if nice_kids_with_presents != total_nice_kids and presents_count == 0:
    print(f"Santa ran out of presents!")

for row in matrix:
    print(*row, sep=' ')

if nice_kids_with_presents == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {abs(nice_kids_with_presents - total_nice_kids)} nice kid/s.")
