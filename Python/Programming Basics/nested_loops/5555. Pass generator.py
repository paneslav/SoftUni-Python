n = int(input())
l = int(input())

for i in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(ord('a'), ord('a') + l):
            for z in range(ord('a'), ord('a') + l):
                for g in range(1, n + 1):
                    if g > i and g > y:
                        print(f"{i}{y}{chr(x)}{chr(z)}{g}", end=' ')