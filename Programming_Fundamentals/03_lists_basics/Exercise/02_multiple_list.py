modifier = int(input())
count = int(input())

counter = modifier

my_list = []

for i in range(count):

    my_list.append(counter)
    counter += modifier

print(my_list) 