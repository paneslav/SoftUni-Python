title = input()
article = input()

divs = []

comment = input()

while comment != 'end of comments':
    divs.append(comment)
    comment = input()

print('<h1>')
print(f'    {title}')
print('</h1>')

print('<article>')
print(f'    {article}')
print('</article>')

for item in divs:
    print('<div>')
    print(f'    {item}')
    print('</div>')