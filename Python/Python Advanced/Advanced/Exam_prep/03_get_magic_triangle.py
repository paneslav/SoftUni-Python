def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    row_to_be_added = 3

    while len(magic_triangle) != n:
        last_row = magic_triangle[-1]
        current_row = [None] * row_to_be_added

        for i in range(len(current_row)):
            if i == 0:
                current_row[i] = 1
            elif i == len(current_row) - 1:
                current_row[i] = 1
            elif i < len(last_row):
                current_row[i] = last_row[i - 1] + last_row[i]

        magic_triangle.append(current_row)
        row_to_be_added += 1

    return magic_triangle


get_magic_triangle(7)
