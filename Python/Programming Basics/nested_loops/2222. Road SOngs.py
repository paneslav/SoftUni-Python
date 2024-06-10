n = int(input())
is_password = False
counter = 0
password = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if a * b + c * d == n:
                        counter += 1
                        if counter == 4:
                            password = f"{a}{b}{c}{d}"
                            is_password = True
                        print(f"{a}{b}{c}{d}", end=' ')
print()
if is_password:
    print(f"Password: {password}")
elif counter == 0:
    print(f"No!")
else:
    print("No!")