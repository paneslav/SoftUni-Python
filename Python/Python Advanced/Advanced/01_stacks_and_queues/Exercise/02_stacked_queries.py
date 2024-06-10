n = int(input())

stack = []

reversed_stack = []

for i in range(n):
    command = input().split()

    action = command[0]

    if action == '1':
        stack.append(int(command[1]))
    elif action == '2' and len(stack) > 0:
        stack.pop(-1)
    elif action == '3' and len(stack) > 0:
        print(max(stack))
    elif action == '4' and len(stack) > 0:
        print(min(stack))

while len(stack) > 0:
    reversed_stack.append(str(stack.pop(-1)))

print(', '.join(reversed_stack))


