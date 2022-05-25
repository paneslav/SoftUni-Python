n = int(input())

if n > 1:


    # middle
    for row in range(1, n + 1):
        for el in range(1, n - row + 1):
            print("", end=' ')
        for col in range(1, row + 1):
            print("* ", end='')
        print()


    for row1 in range(n - 1, 1, -1):
        for el1 in range(n - row1 + 1, 1, -1):
            print("", end=' ')
        for col1 in range(row1 + 1,1, -1):
            print("* ", end='')
        print()

    for row3 in range(1, n - 1):
        print("", end=' ')
    print(" *")



else:
    print("*")