number = input()

sorted_number = sorted(number, reverse=True)


for index in range(len(number)):
    print(sorted_number[index], end='')