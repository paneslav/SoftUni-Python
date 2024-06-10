import sys

num = input()
max_num = -sys.maxsize

while num != "Stop":
    number = int(num)

    if number > max_num:
        max_num = number

    num = input()

print(f"{max_num}")