rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    if command[0] == 'swap' and len(command) == 5:
        if int(command[1]) < rows and int(command[2]) < cols and int(command[3]) < rows and int(command[4]) < cols:
            x1 = int(command[1])
            y1 = int(command[2])
            x2 = int(command[3])
            y2 = int(command[4])


            a = matrix[x1][y1]
            b = matrix[x2][y2]

            matrix[x1][y1] = b
            matrix[x2][y2] = a
            for row in matrix:
                print(' '.join(str(x) for x in row))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
