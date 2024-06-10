n = input()

sum_prime = 0
sum_nonprime = 0

counter = 0
is_prime = False

while n != "stop":
    number = int(n)

    if number == 2 or number == 3 or number == 5 or number == 7 or number == 0:
        is_prime = True
    elif number < 0:
        print("Number is negative.")
        number = 0
    else:
        if number % 1 == 0:
            counter += 1
        if number % 2 == 0:
            counter += 1
        if number % 3 == 0:
            counter += 1
        if number % 5 == 0:
            counter += 1
        if number % 7 == 0:
            counter += 1
        if number % 9 == 0:
            counter += 1
        if number % number == 0:
            counter += 1

    if counter < 3:
        is_prime = True

    if is_prime:
        sum_prime += number
    else:
        sum_nonprime += number

    is_prime = False
    counter = 0
    n = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")