initial_string = input()

reversed_string = ''

stack = []

for char in initial_string:
    stack.append(char)

while stack:
    reversed_string += stack.pop()

print(reversed_string)