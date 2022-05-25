n = int(input())

outer_dashes = (n - 1) // 2
mid_dashes = 0

mid_stars = 2 if n % 2 == 0 else 1

range1 = ((n + 1) // 2) - 1

if n % 2 == 0:
    mid_dashes = 2
else:
    mid_dashes = 1

if n == 1:
    print("*")
elif n == 2:
    print("**")
else:
    print(f"{'-' * outer_dashes}{'*' * mid_stars}{'-' * outer_dashes}")

    for i in range(range1):
        print(f"{'-' * (outer_dashes - 1)}*{'-' * mid_dashes}*{'-' * (outer_dashes - 1)}")

        if i == range1 - 1:
            break
        outer_dashes -= 1
        mid_dashes += 2

    for y in range(range1):

        if y == range1 - 1:
            break
        outer_dashes += 1
        mid_dashes -= 2
        print(f"{'-' * (outer_dashes - 1)}*{'-' * mid_dashes}*{'-' * (outer_dashes - 1)}")

    print(f"{'-' * outer_dashes}{'*' * mid_stars}{'-' * outer_dashes}")