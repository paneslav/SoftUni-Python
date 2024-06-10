type = input()
rows = int(input())
columns = int(input())

if type == "Premiere":
    print(f"{(rows*columns) * 12.00:.2f} leva")
elif type == "Normal":
    print(f"{(rows*columns) * 7.50:.2f} leva")
else:
    print(f"{(rows*columns) * 5.00:.2f} leva")