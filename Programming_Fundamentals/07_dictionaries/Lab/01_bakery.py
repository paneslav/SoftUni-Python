elements = input().split()
stock = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}

print(stock)