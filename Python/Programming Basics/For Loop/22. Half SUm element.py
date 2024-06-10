import sys

n = int(input())

sum = 0
biggest = -sys.maxsize

for i in range(1, n + 1):
    number = int(input())

    if number > biggest:
        biggest = number

    sum += number

if sum - biggest == biggest:
    print(f"Yes\nSum = {biggest}")
else:
    print(f"No\nDiff = {abs(biggest - (sum - biggest))}")