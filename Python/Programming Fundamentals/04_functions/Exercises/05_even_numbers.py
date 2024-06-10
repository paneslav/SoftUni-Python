def check_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = list(map(int, input().split()))
even_numbers = list(filter(check_even, numbers))

print(even_numbers)