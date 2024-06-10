n = int(input())

for i in range(n):
    command = input()
    name = ''
    age = ''

    for index in range(len(command)):
        if command[index] == '@':
            for nested_index in range(index + 1, len(command)):
                if command[nested_index] == '|':
                    break
                name += command[nested_index]
        elif command[index] == '#':
            for nested_index in range(index + 1, len(command)):
                if command[nested_index] == '*':
                    break
                age += command[nested_index]

    print(f"{name} is {age} years old.")


# number_strings = int(input())
#
# for _ in range(number_strings):
#     test_string = input()
#     # if all([test_string.count("@") == 1, test_string.count("|") == 1,
#     #         test_string.count("#") == 1, test_string.count("*") == 1]):
#     name = test_string[test_string.index("@") + 1:test_string.index("|")]
#     age = test_string[test_string.index("#") + 1:test_string.index("*")]
#     print(f"{name} is {age} years old.")