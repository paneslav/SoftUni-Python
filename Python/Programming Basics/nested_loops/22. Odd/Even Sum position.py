first_num = int(input())
second_num = int(input())

odd_sum = 0
even_sum = 0
num_position = 1

for i in range(first_num, second_num + 1):

    for index, value in enumerate(str(i)):
        # num = int(char)
        if index % 2 == 0:
            even_sum += int(value)
        else:
            odd_sum += int(value)

        # num_position += 1

    if even_sum == odd_sum:
        print(i, end=" ")

    odd_sum = 0
    even_sum = 0

