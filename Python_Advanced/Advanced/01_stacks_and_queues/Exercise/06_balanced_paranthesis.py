parantheses = input()

stack = []

result = 0

for i in range(len(parantheses)):
    if parantheses[i] == '{' or parantheses[i] == '[' or parantheses[i] == '(':
        stack.append(i)
    else:

        if not stack:
            print(f"NO")
            exit()

        top_element = parantheses[stack[-1]]

        if parantheses[i] == ')' and top_element == '(':
            stack.pop()
        elif parantheses[i] == '}' and top_element == '{':
            stack.pop()
        elif parantheses[i] == ']' and top_element == '[':
            stack.pop()
        else:
            break

if stack:
    print(f"NO")
else:
    print(f"YES")

