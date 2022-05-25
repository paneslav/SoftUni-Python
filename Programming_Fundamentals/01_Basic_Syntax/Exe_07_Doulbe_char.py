while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    for i in range(len(command)):
        double_word = command[i] * 2
        print(double_word, end='')

    print()