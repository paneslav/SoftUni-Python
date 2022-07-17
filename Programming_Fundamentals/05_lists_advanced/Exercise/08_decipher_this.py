decipher_this = input().split()

num = ''

for item in decipher_this:
    for c in item:
        if c.isdigit():
            num += c

    item_without_number = item[len(num):]
    item_without_number = list(item_without_number)
    item_without_number[0], item_without_number[-1] = item_without_number[-1], item_without_number[0]
    item_without_number = ''.join(item_without_number)
    print(chr(int(num)) + item_without_number, end= ' ')
    num = ''
    item_without_number = ''