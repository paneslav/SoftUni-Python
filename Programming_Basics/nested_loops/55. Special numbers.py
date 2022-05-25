n = int(input())
is_special = False

for i in range(1, 10):
    for y in range(1, 10):
        for x in range(1, 10):
            for g in range(1, 10):
                if n % i == 0 and n % y == 0 and n % x == 0 and n % g == 0:
                    print(f"{i}{y}{x}{g}", end=" ")