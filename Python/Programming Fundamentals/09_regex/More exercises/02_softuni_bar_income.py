import re

pattern = r'%([A-Z][a-z]+)%[^|$%\.]*?<(\w+)>[^|$%\.]*?\|(\d+)\|[^|$%\.]*?([1-9][0-9]*\.?\d*)\$'
total_income = 0

while True:
    command = input()

    if command == 'end of shift':
        break

    result = re.search(pattern, command)

    if not result:
        continue

    customer, product, count, price = result.groups()

    print(f"{customer}: {product} - {int(count) * float(price):.2f}")
    total_income += int(count) * float(price)

print(f"Total income: {total_income:.2f}")