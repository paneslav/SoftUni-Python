n = int(input())

total_possible = 0

for i in range(0, n + 1):
    for y in range(0, n + 1):
        for x in range(0, n + 1):
            if i + y + x == n:
                total_possible += 1

print(total_possible)