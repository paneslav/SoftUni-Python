data_to_modify = input().split()


while True:

    command = input().split()
    result = ''

    if command[0] == '3:1':
        break

    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < len(data_to_modify) and end_index < len(data_to_modify):
            for i in range(start_index, end_index + 1):
                result += data_to_modify[i]
            del data_to_modify[start_index:end_index + 1]
            data_to_modify.insert(start_index, result)
        elif len(data_to_modify) > start_index:
            for i in range(start_index, len(data_to_modify)):
                result += data_to_modify[i]
            del data_to_modify[start_index:end_index + 1]
            data_to_modify.insert(start_index, result)

    elif command[0] == 'divide':
        index_to_divide = int(command[1])
        word = data_to_modify[index_to_divide]
        index_of_word = data_to_modify.index(word)
        partitions = int(command[2])

        divided_item = ''
        data_to_modify.remove(word)

        if len(word) % partitions == 0:
            start_index = 0
            end_index = int(len(word) / partitions)
            for i in range(partitions):
                divided_item = ''
                divided_item += word[start_index:end_index]
                start_index += 2
                end_index += 2
                data_to_modify.insert(index_of_word, divided_item)
                index_of_word += 1

        else:
            pass


print(*data_to_modify)