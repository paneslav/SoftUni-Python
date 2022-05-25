hundreds_cap = int(input())
tens_cap = int(input())
ones_cap = int(input())

is_prime = False
counter = 0
total_count = 0

for i in range(1, hundreds_cap + 1):
    for x in range(2, tens_cap + 1):

        for num in range(2, x):
            if x % num == 0:
                is_prime = True


        if not is_prime:
            for y in range(1, ones_cap + 1):
                if i % 2 == 0 and y % 2 == 0 and not is_prime:
                    print(f"{i} {x} {y}")

        is_prime = False