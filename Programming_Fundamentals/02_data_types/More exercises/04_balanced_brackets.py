n = int(input())
my_list = []

isBalanced = False

for i in range(n):
    string = input()
    if '(' in string or ')' in string:
        my_list.append(string)

if len(my_list) % 2 == 0:
    for index in range(len(my_list)):
        if index % 2 == 0 and my_list[index] == '(':
            isBalanced = True
        if index % 2 != 0 and my_list[index] != ')':
            isBalanced = False

if isBalanced:
    print("BALANCED")
else:
    print("UNBALANCED")



# n = int(input())
#
# final_word = ''
#
# start = '('
# end = ')'
#
# isBalanced = False
# start_counter = 0
# end_counter = 0
#
# for i in range(n):
#
#     current_string = input()
#     final_word += current_string
#
# for index in range(len(final_word)):
#
#     if str(final_word)[index] == start:  # search for '('
#
#         start_counter += 1
#         if start_counter > 1 and end_counter == 0:
#             isBalanced = False
#             break
#         continue
#
#     if str(final_word)[index] == end:  # search for ')'
#
#         end_counter += 1
#         isEnded = True
#         if end_counter > start_counter:
#             isBalanced = False
#             break
#         elif end_counter == start_counter:
#             isBalanced = True
#
# if isBalanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")