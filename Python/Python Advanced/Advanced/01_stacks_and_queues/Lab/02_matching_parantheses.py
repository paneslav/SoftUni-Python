initial_string = input()

stack = []

for index in range(len(initial_string)):
    if initial_string[index] == '(':
        stack.append(index)
    elif initial_string[index] == ')':
        start_index = stack.pop()
        expression = initial_string[start_index:index + 1]
        print(expression)