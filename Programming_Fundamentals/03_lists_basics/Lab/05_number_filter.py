n = int(input())

COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

my_list = []
modified_list = []

for i in range(n):

    number = int(input())
    my_list.append(number)

command = input()

filter_command = False

for index in range(len(my_list)):

    filter_command = (
        (command == COMMAND_EVEN and my_list[index] % 2 == 0) or
        (command == COMMAND_ODD and my_list[index] % 2 != 0) or
        (command == COMMAND_POSITIVE and my_list[index] >= 0) or
        (command == COMMAND_NEGATIVE and my_list[index] < 0)
    )

    if filter_command:
        modified_list.append(my_list[index])

print(modified_list)