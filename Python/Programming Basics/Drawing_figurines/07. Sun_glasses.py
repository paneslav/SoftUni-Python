count = int(input())

# top
print(f"{'*' * count*2}{' ' * count}{'*' * count*2}")

# mid
for i in range(1, count - 1):
    if count % 2 == 0:
        if i == (count) / 2 - 1:
            print(f"*{'/' * (count * 2 - 2)}*{'|' * count}*{'/' * (count * 2 - 2)}*")
            continue
    else:
        if i == (count - 1) / 2:
            print(f"*{'/' * (count * 2 - 2)}*{'|' * count}*{'/' * (count * 2 - 2)}*")
            continue

    print(f"*{'/' * (count * 2 - 2)}*{' ' * count}*{'/' * (count*2 -2)}*")

# bot
print(f"{'*' * count*2}{' ' * count}{'*' * count*2}")