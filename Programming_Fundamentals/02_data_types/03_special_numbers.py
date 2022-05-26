n = int(input())

digits_sum = 0
number_string = ''
current_digit = 0

isSpecial = False

for number in range(1, n + 1):

    number_string = str(number)

    for i in range(len(number_string)):
        current_digit = int(number_string[i])
        digits_sum += current_digit

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        isSpecial = True

    print(f"{number} -> {isSpecial}")

    isSpecial = False
    digits_sum = 0