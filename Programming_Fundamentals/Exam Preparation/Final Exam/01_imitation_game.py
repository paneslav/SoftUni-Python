message = input()

while True:
    command = input().split('|')
    if command[0] == 'Decode':
        print(f"The decrypted message is: {message}")
        break

    action = command[0]

    if action == 'ChangeAll':
        substring = command[1]
        replacement = command[-1]
        message = message.replace(substring, replacement)

    elif action == 'Insert':
        index = int(command[1])
        char_to_insert = command[-1]
        message = message[:index] + char_to_insert + message[index:]

    elif action == 'Move':
        number_of_letters = int(command[1])
        message = message[number_of_letters:] + message[:number_of_letters]

