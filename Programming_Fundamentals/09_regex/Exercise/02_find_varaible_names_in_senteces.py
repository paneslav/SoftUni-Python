import re

line = input()
counter = 0
pattern = r'\b_([a-zA-Z0-9]+)\b'

result = re.findall(pattern, line)

print(','.join(result))

