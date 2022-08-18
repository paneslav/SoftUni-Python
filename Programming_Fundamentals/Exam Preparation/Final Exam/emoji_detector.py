import re

cool_treshold = 1
text = input()

emoji_pattern = r'(:{2}|\*{2})([A-Z]{1}[a-z]{2,})\1'
numbers_pattern = r'\d'

emoji_match = re.findall(emoji_pattern, text)
numbers_match = re.findall(numbers_pattern, text)

for digit in numbers_match:
    cool_treshold *= int(digit)

# for item in emoji_match:
#     print(item.group(2))

print(f'Cool threshold: {cool_treshold}')
print(f'{len(emoji_match)} emojis found in the text. The cool ones are:')
for item in emoji_match:
    emoji_coolnes = 0
    for char in item[-1]:
        emoji_coolnes += ord(char)
    if emoji_coolnes >= cool_treshold:
        print(f'{item[0]}{item[-1]}{item[0]}')
