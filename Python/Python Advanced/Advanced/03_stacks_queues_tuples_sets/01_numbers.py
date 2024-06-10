first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for i in range(n):
    command = input().split()

    if command[0] == 'Add':

        if command[1] == 'First':
            first_sequence = first_sequence.union([int(x) for x in command[2:]])
        else:
            second_sequence = second_sequence.union([int(x) for x in command[2:]])

    elif command[0] == 'Remove':

        if command[1] == 'First':
            first_sequence = first_sequence.difference([int(x) for x in command[2:]])
        else:
            second_sequence = second_sequence.difference([int(x) for x in command[2:]])

    elif command[0] == 'Check':
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))


print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')