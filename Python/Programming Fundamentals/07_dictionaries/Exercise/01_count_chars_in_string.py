from collections import defaultdict

text = input()

occ_dict = defaultdict(int)

for char in text:
    if char != ' ':
        occ_dict[char] += 1

text_to_print = [f'{item} -> {occ_dict[item]}' for item in occ_dict]
print('\n'.join(text_to_print))