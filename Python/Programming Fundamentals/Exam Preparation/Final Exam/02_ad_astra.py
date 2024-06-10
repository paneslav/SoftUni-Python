import re

text = input()

pattern = r'(#|\|)([a-zA-Z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1'

match = re.findall(pattern, text)

total_nutrition = 0

for item in match:
    total_nutrition += int(item[-1])

days_to_live = total_nutrition // 2000

print(f"You have food to last you for: {days_to_live} days!")

if match:
    for food in match:
        print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[-1]}")
