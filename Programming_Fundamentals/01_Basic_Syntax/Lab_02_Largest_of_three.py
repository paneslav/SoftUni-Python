import sys

largest = -sys.maxsize

for _ in range(3):
    number = int(input())

    if number > largest:
        largest = number

print(largest)



