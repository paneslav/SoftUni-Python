import re

line = input()

pattern = r'\d+'

result = []

while line:
    result += re.findall(pattern, line)
    line = input()

print(' '.join(result))