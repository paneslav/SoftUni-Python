def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(subtract(sum_numbers(num_1, num_2), num_3))