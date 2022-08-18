elements = input().split()

moves = 0

while True:
    moves += 1
    outOfBonds = False
    command = input().split()
    if command[0] == 'end':
        if len(elements) != 0:
            print(f"Sorry you lose :(")
            print(' '.join(elements))
        break

    first_index = int(command[0])
    second_index = int(command[1])

    try:
        elements[first_index]
        elements[second_index]
    except IndexError:
        outOfBonds = True

    if first_index == second_index or outOfBonds or (first_index < 0 or second_index < 0):
        index_to_insert = len(elements) // 2
        string_to_insert = f'-{moves}a'
        elements.insert(index_to_insert, string_to_insert)
        elements.insert(index_to_insert, string_to_insert)
        print(f"Invalid input! Adding additional elements to the board")
        continue

    if elements[first_index] == elements[second_index]:
        # elements.pop(first_index)
        print(f"Congrats! You have found matching elements - {elements.pop(first_index)}!")
        if second_index != 0:
            elements.pop(second_index - 1)
        else:
            elements.pop(second_index)
    else:
        print(f"Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break