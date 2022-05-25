import sys

divisor = int(input())
boundary = int(input())

largest = -sys.maxsize
for i in range(1, boundary + 1):

    if i % divisor == 0 and boundary >= i > 0:
        if i > largest:
            largest = i

print(largest)