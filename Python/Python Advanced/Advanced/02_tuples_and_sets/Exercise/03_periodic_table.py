n = int(input())

elements = set()

for _ in range(n):
    current_elements = input().split()

    for element in current_elements:
        if element not in elements:
            elements.add(element)

[print(item) for item in elements]