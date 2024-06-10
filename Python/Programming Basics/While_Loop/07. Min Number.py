import sys

num = input()
min_num = sys.maxsize

while num != "Stop":
    number = int(num)

    if min_num > number:
        min_num = number

    num = input()

print(f"{min_num}")