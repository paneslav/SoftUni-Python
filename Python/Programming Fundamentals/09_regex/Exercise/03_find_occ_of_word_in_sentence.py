import re

sentence = input()
word_to_count = input()


result = re.findall(fr'{word_to_count}\b', sentence, re.IGNORECASE)

print(len(result))