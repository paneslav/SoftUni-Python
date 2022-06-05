word = input().split(' ')

modified_list = []

for i in range(len(word)):

    modified_list.append(-int(word[i]))

print(modified_list)