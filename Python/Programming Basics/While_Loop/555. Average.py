n = int(input())

sum = 0
for i in range(1, n + 1):
    number = float(input())
    sum += number

print(f"{sum/n:.2f}")