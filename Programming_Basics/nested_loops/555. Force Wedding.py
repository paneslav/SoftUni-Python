men = int(input())
women = int(input())
max_tables = int(input())

for i in range(1, men + 1):
    for x in range(1, women + 1):
        if max_tables <= 0:
            break
        print(f"({i} <-> {x})", end=' ')
        max_tables -= 1


