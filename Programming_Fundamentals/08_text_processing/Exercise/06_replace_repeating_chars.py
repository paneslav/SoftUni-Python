user_input = input()

filtered_chars = []

current_string = ''
for char in user_input:
    current_string += char
    if current_string[0] != char:
        user_input = user_input.replace(current_string[:len(current_string) - 1], current_string[0])
        current_string = char

if len(current_string) > 1:
    user_input = user_input.replace(current_string, current_string[0])
    
print(user_input)