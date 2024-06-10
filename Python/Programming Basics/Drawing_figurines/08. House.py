n = int(input())

stars = 0
dashes = (n - 1) // 2
counter = 0

if n % 2 == 0:
    stars = 2
else:
    stars = 1

for i in range((n + 1) // 2):
    print(f"{'-' * dashes}{'*' * stars}{'-' * dashes}")

    stars += 2
    dashes -= 1

for y in range((n//2)):
    print(f"|{'*' * (n - 2)}|")

