words = input().split()

while True:
    command = input().split()

    if command[0] == 'Stop':
        break

    action = command[0]

    if action == 'Delete':
        item_to_delete = int(command[-1]) + 1
        if 0 <= item_to_delete < len(words):
            words.pop(item_to_delete)

    elif action == 'Swap':
        first_word = command[1]
        second_word = command[-1]

        if first_word in words and second_word in words:
            first_index = words.index(first_word)
            second_index = words.index(second_word)
            words[first_index], words[second_index] = words[second_index], words[first_index]

    elif action == 'Put':
        word_to_insert = command[1]
        where_to_insert = int(command[-1]) - 1

        if len(words) >= where_to_insert >= 0:
            words.insert(where_to_insert, word_to_insert)

    elif action == 'Sort':
        words = sorted(words, reverse=True, key=str.lower)
        # words.sort(reverse=True)

    elif action == 'Replace':
        first_word = command[1]
        second_word = command[-1]

        if second_word in words:
            second_word_index = words.index(second_word)
            words[second_word_index] = first_word

print(' '.join(words))
