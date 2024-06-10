size = int(input())
matrix = [[x for x in input()] for row in range(size)]
symbol = input()

is_found = False

for row in range(size):
    for col in range(size):
        if symbol == matrix[row][col]:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")