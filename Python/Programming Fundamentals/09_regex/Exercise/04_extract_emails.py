import re

e_mails = input()

pattern = r'(?<=\s)([a-z0-9]+[\.\-\_a-z0-9]*@[a-z\-]+(\.[a-z]+)+)\b'

result = re.findall(pattern, e_mails)

for item in result:
    print(item[0])