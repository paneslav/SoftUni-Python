import re
dates = input()

pattern = r'\b(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(pattern, dates)

for item in result:
    print(f"Day: {item[0]}, Month: {item[2]}, Year: {item[-1]}")