n = int(input())

for i in range(97, 97 + n):
    for y in range(97, 97 + n):
        for z in range(97, 97 + n):
            print(f"{chr(i)}{chr(y)}{chr(z)}")