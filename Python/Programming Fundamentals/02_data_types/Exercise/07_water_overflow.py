n = int(input())

total_liters = 0

for i in range(n):

    liters = int(input())
    total_liters += liters

    if total_liters > 255:
        total_liters -= liters
        print("Insufficient capacity!")

print(total_liters)
    