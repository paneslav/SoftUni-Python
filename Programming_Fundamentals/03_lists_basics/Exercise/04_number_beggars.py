money_list = input().split(", ")
beggars = int(input())

counter = 0

modified_list = [0] * beggars

for element in money_list:

    if counter == beggars:
        counter = 0
    modified_list[counter] += int(element)
    counter += 1

print(modified_list)