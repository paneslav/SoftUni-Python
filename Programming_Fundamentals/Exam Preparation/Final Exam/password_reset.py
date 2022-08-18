data = input()

final_result = ''

while True:
    command = input().split()
    if command[0] == 'Done':
        print(f'Your password is: {data}')
        break

    if command[0] == 'TakeOdd':
        data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
        print(data)

    elif command[0] == 'Cut':
        start = int(command[1])
        length = int(command[-1])
        data = data[:start] + data[start + length:]
        print(data)
        # for i in range(length):
        #     final_result = list(final_result)
        #     final_result.pop(start)
        # final_result = ''.join(final_result)

    elif command[0] == 'Substitute':
        char_to_replace = command[1]
        replacement = command[-1]
        if char_to_replace in data:
            data = data.replace(char_to_replace, replacement)
            print(data)
        else:
            print('Nothing to replace!')