user_input = input()

final_output = ''

for char in user_input:
    final_output += chr(ord(char) + 3)

print(final_output)