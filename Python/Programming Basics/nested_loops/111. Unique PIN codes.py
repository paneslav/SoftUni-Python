first_top = int(input())
second_top = int(input())
third_top = int(input())

is_even_first = False
is_even_second = False
is_prime = False

for i in range(2, first_top+1):
    for x in range(2, second_top + 1):
        for y in range(2, third_top+1):
            if i % 2 == 0:
                is_even_first = True
            if y % 2 ==0:
                is_even_second = True
            if x == 2 or x == 3 or x == 5 or x == 7:
                is_prime = True

            if is_even_first and is_even_second and is_prime:
                print(f"{i} {x} {y}")

            is_even_first = False
            is_even_second = False
            is_prime = False

