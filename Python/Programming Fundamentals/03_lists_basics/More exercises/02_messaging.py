number_sequences = input().split()
message = input()
message_length = len(message)
char_indexes = [message[i] for i in range(len(message))]

char_to_print = ''
current_sequence = ''

for number in number_sequences:

    current_sequence = number
    sequence_total = 0

    for index in range(len(number)):  # find sequence sum - index
        sequence_total += int(number[index])

    if sequence_total > message_length:
        char_to_print = char_indexes[sequence_total - message_length]
    else:
        char_to_print = char_indexes[sequence_total]

    char_indexes.remove(char_to_print)

    print(char_to_print, end='')