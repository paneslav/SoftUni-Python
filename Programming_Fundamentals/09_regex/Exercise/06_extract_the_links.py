import re

pattern = r'((w{3})\.([a-zA-Z0-9\-]+)(\.[a-z]+)+)'

valid_urls = []

line = input()

while line:
    match = re.search(pattern, line)
    if match:
        valid_urls.append(match.group(0))
    line = input()

for item in valid_urls:
    print(item)