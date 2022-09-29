rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    for col in range(cols):
        matrix.append(f"{chr(97 + row)}{chr((97 + row) + col)}{chr(97 + row)}")
    print(' '.join(matrix))
    matrix = []