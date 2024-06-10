import sys

n = int(input())
greater = -sys.maxsize
lesser = sys.maxsize
for i in range(0, n, +1):
    number = int(input())
    if number > greater:
        greater = number
    if number < lesser:
        lesser = number

print(f"Max number: {greater}")
print(f"Min number: {lesser}")