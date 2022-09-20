from collections import deque

expression = input().split()

calculations = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

for char in expression:
    if char in "*+-/":
        operation = char

        while len(calculations) > 1:
            left = calculations.popleft()
            right = calculations.pop()

            calculations.appendleft(operations[operation](left, right))

    else:
        calculations.append(int(char))

print(calculations[0])