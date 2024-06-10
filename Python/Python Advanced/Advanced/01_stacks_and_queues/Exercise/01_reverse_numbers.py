num_stack = list(map(int, input().split()))

while num_stack:
    print(num_stack.pop(-1), end=' ')