numbers_list = list(map(int, input().split(', ')))

even_numbers_list = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]

# for index in range(len(numbers_list)):
#     if numbers_list[index] % 2 == 0:
#         even_numbers_list.append(index)
#
# print(numbers_list)

print(even_numbers_list)
