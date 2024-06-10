n = int(input())
key_word = input()

my_list = []
modified_list = []

for i in range(n):

    sentence = input()
    my_list.append(sentence)

    if key_word in sentence:
        modified_list.append(sentence)

print(my_list)
print(modified_list)