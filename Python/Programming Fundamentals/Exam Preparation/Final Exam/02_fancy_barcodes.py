import re

n = int(input())
pattern = r'@#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z]{1})@{1}#{1,}'

for _ in range(n):
    barcode = input()
    match = re.search(pattern, barcode)
    product_group = ''
    if match:
        if match.group(1).isalpha():
            product_group = '00'
        for char in match.group(1):
            if char.isdigit():
                product_group += char

        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")