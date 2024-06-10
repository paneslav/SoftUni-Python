couples = int(input())

sum = 0
totalSum = 0
preLast = 0
last = 0

for i in range(1, couples + 1):
    a = float(input())
    b = float(input())
    sum = a + b
    totalSum += sum

    if i == couples - 1:
        preLast = sum
    elif i == couples:
        last = sum

if totalSum / couples == sum:
    print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={abs(preLast-last)}")