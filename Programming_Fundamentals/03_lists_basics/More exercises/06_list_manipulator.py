import sys

string_input = input().split()

numbers_input = [int(i) for i in string_input]

while True:

    max_number = -sys.maxsize
    min_number = sys.maxsize
    current_action = input().split()
    if current_action[0] == 'end':
        break
    current_index = 0
    even_numbers = [i for i in numbers_input if i % 2 == 0]  # adds all the even numbers
    odd_numbers = [i for i in numbers_input if i % 2 != 0]  # adds all the odd numbers
    copy_even_numbers = even_numbers.copy()
    copy_odd_numbers = odd_numbers.copy()
    copy_even_numbers.reverse()
    copy_odd_numbers.reverse()

    if current_action[0] == "exchange":
        current_index = int(current_action[1])
        if current_index >= len(numbers_input) or current_index < 0:
            print("Invalid index")
        else:
            numbers_input = numbers_input[current_index + 1:] + numbers_input[:current_index + 1]

    elif current_action[0] == "max":
        if current_action[1] == "even":
            if len(even_numbers) == 0:
                print("No matches")
                continue
            for number in numbers_input:  # checks for max even number
                if number == 0:
                    continue
                if number >= max_number and number % 2 == 0:
                    max_number = number
            print(numbers_input.index(max_number))
        else:
            if len(odd_numbers) == 0:
                print("No matches")
                continue
            for number in numbers_input:  # checks for max odd number
                if number == 0:
                    continue
                if number >= max_number and number % 2 != 0:
                    max_number = number
            print(numbers_input.index(max_number))

    elif current_action[0] == "min":
        if current_action[1] == "even":
            if len(even_numbers) == 0:
                print("No matches")
                continue
            for number in numbers_input:  # checks for min even number
                if number == 0:
                    continue
                if number <= min_number and number % 2 == 0:
                    min_number = number
            print(numbers_input.index(min_number))
        else:
            if len(odd_numbers) == 0:
                print("No matches")
                continue
            for number in numbers_input:  # checks for min odd number
                if number == 0:
                    continue
                if number <= min_number and number % 2 != 0:
                    min_number = number
            print(numbers_input.index(min_number))

    elif current_action[0] == "first":
        current_index = int(current_action[1])
        if current_action[2] == "even":
            if current_index > len(numbers_input):
                print("Invalid count")
            else:
                print(even_numbers[:current_index])
        else:
            if current_index > len(numbers_input):
                print("Invalid count")
            else:
                print(odd_numbers[:current_index])

    elif current_action[0] == "last":
        current_index = int(current_action[1])
        if current_action[2] == "even":
            if current_index > len(numbers_input):
                print("Invalid count")
            else:
                if current_index >= len(even_numbers):
                    print(even_numbers)
                else:
                    copy_even_numbers = copy_even_numbers[:current_index]
                    copy_even_numbers.reverse()
                    print(copy_even_numbers)
        else:
            if current_index > len(numbers_input):
                print("Invalid count")
            else:
                if current_index >= len(odd_numbers):
                    print(odd_numbers)
                else:
                    copy_odd_numbers = copy_odd_numbers[:current_index]
                    copy_odd_numbers.reverse()
                    print(copy_odd_numbers)

print(numbers_input)