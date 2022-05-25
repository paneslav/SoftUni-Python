n = int(input())

oddSum = 0
evenSum = 0

for i in range(1, n + 1):
    number = int(input())
    if i % 2 == 0:
        evenSum += number
    else:
        oddSum += number

if evenSum == oddSum:
    print(f"Yes\nSum = {evenSum}")
else:
    print(f"No\nDiff = {abs(evenSum-oddSum)}")
