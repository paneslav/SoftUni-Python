import re

html = input()

title_pattern = r'<title>(.+)<\/title>'
body_pattern = r'<body>(.+)<\/body>'

counter = 0

clean_body = ''

title_match = re.search(title_pattern, html)
body_match = re.search(body_pattern, html)

body = body_match.group(1)

if '\\n' in body:
    body = body.replace('\\n', '')

while counter != len(body):
    if body[counter] == '<':
        for i in range(counter, len(body)):
            if body[i] == '>':
                counter += (i - counter) + 1
                break
    else:
        clean_body += body[counter]
        counter += 1

print(f'Title: {title_match.group(1)}')
print(f'Content: {clean_body}')
