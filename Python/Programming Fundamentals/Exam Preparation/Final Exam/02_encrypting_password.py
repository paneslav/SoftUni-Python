import re

n = int(input())

pattern = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for i in range(n):
    text = input()
    password = ''
    match = re.search(pattern, text)
    if match:
        password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
        print(f"Password: {password}")
    else:
        print(f"Try another password!")