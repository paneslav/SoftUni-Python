user_input = input()

for char in user_input:
    if char == ':':
        print(f":{user_input[user_input.index(char) + 1]}")
        user_input = user_input.replace(char, '', 1)