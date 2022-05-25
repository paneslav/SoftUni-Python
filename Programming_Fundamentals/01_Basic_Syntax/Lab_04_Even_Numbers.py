n = int(input())

is_odd = False

for _ in range(n):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        is_odd = True
        break
else:
    print("All numbers are even.")