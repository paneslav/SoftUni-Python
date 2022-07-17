# words_list = input().lower().split()
#
# words_dictionary = {item: int(words_list.count(item)) for item in words_list}
#
# words_to_print = []
#
# for item in words_dictionary:
#     if words_dictionary[item] % 2 != 0:
#         words_to_print.append(item)
#
# print(' '.join(words_to_print))
from collections import defaultdict

words = input().lower().split()

words_dict = defaultdict(int)

for word in words:
    words_dict[word] += 1

words_to_print = [word for word, value in words_dict.items() if value % 2 != 0]
print(' '.join(words_to_print))