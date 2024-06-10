n = int(input())

leftSum = 0
rightSum = 0

for i in range(1, 2*n +1, 1):
    number = int(input())
    if i <= n:
        rightSum += number
    else:
        leftSum += number


if leftSum == rightSum:
    print(f"Yes, sum = {leftSum}")
else:
    print(f"No, diff = {abs(leftSum-rightSum)}")