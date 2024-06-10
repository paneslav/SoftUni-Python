import re

pattern = r'>>([a-zA-Z]*)<<(\d+\.?\d*)!(\d+)'

total_money = 0
bought_furniture = []
while True:
    command = input()
    if command == 'Purchase':
        break
    result = re.findall(pattern, command)
    if not result:
        continue
    bought_furniture.append(result[0][0])
    total_money += float(result[0][1]) * int(result[0][-1])

print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_money:.2f}")
