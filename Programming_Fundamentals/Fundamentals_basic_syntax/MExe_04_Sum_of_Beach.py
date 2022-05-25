string = input().lower()

counter = 0
words = ['sand', 'water', 'fish', 'sun']

for word in words:
    counter += string.count(word)

print(counter)