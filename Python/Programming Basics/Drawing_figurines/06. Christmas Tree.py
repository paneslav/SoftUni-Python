count = int(input())

for i in range(1, count):
    print(f"{' ' * (count - i)}{'* ' * i}")
for y in range(count, 0, -1):
    print(f"{' ' * (count - y)}{'* ' * y}")




# for i in range(count + 1):
    # print(f"{' ' * (count - i)}{'*' * i} | {'*' * i}")