import re

pattern = r'(=|/)([A-Z]{1}[a-zA-Z]{2,})\1'

text = input()
match = re.finditer(pattern, text)

destinations = []
travel_points = 0
for item in match:
    travel_points += len(item.group(2))
    destinations.append(item.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")