first_initial = int(input())
second_initial = int(input())
first_end = int(input()) + first_initial
second_end = int(input()) + second_initial

is_first_prime = False
is_second_prime = False

for i in range(first_initial, first_end + 1):
    for num1 in range(2, i):
        if i % num1 == 0:
            is_first_prime = True

    for y in range(second_initial, second_end + 1):

        for num2 in range(2, y):
            if y % num2 == 0:
                is_second_prime = True

        if not is_first_prime and not is_second_prime:
            print(f"{i}{y}")
        is_second_prime = False

    is_first_prime = False