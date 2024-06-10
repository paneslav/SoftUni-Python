first_item, second_item = input().split()
result = 0
counter = 0

for i in range(len(first_item)):
    if i > len(second_item) - 1:
        break
    result += ord(first_item[i]) * ord(second_item[i])
    counter += 1


if len(second_item) > len(first_item):
    for char in second_item[counter:]:
        result += ord(char)
else:
    for char in first_item[counter:]:
        result += ord(char)

print(result)