string = input()

capitals = []

for index in range(len(string)):

    if string[index].isupper():
        capitals.append(index)

print(capitals)