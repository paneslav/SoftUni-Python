def check_smallest_number(a, b, c):
    numbers_list = [a, b ,c]
    min_number = min(numbers_list)
    return min_number


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(check_smallest_number(number_1, number_2, number_3))