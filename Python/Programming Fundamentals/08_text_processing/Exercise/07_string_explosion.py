user_input = list(input())
counter = 0
start_from = 0
strength = 0

toAdd = False
for char in user_input:

    if char == '>':
        if counter == 0:
            start_from = user_input.index(char)
        else:
            start_from = char_index + 1

        char_index = user_input.index(char, start_from)

        if toAdd:
            chars_to_delete = int(user_input[char_index + 1]) + strength
            strength = 0
            toAdd = False
        else:
            chars_to_delete = int(user_input[char_index + 1])

        for i in range(chars_to_delete):
            if user_input[-1] == '>':
                break
            if user_input[char_index + 1] != '>':
                user_input.pop(char_index + 1)
            else:
                strength += chars_to_delete - i
                toAdd = True
                break
        counter += 1

print(''.join(user_input))


# text = input().split(">")
# strenght = 0
# unused = 0
#
# for i in range(len(text)):
#     strenght = text[i][0]
#     if strenght.isdigit():
#         strenght = int(strenght)
#         strenght = strenght + unused
#         unused = strenght - len(text[i])
#
#         if strenght > len(text[i]):
#             strenght = len(text[i])
#
#         text[i] = text[i][strenght::]
#         if unused < 0:
#             unused = 0
#
# print(*text, sep=">")