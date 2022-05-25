n = int(input())

print("+", end=' ')
for x in range(1, (n - 2) + 1):
    print("-", end=' ')
print("+")

for i in range(1, (n - 2) + 1):
    print("|", end=' ')
    for y in range(1, n - 2 + 1):
        print("-", end=' ')
    print("|")

print("+", end=' ')
for x in range(1, (n - 2) + 1):
    print("-", end=' ')
print("+")
