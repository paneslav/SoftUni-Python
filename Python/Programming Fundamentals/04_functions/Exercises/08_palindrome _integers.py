def check_for_palindromes(number):

    for num in number:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
check_for_palindromes(numbers)