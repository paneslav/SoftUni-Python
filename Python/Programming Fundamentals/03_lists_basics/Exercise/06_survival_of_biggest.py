list_of_numbers = input().split()
numbers_to_pop = int(input())

int_list = []

for element in list_of_numbers:
    int_list.append(int(element))

for i in range(numbers_to_pop):
    int_list.remove(min(int_list))

print(*int_list, sep=', ')