from collections import defaultdict

junk_items_dict = defaultdict(int)
key_items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
itemOver250 = False

while True:
    if itemOver250:
        break
    command = input().lower().split()
    for i in range(0, len(command), 2):
        quantity = int(command[i])
        resource = command[i + 1]

        if resource not in key_items_dict:
            junk_items_dict[resource] += quantity
        else:
            key_items_dict[resource] += quantity

        if (key_items_dict['shards'] >= 250) or (key_items_dict['fragments'] >= 250) or (key_items_dict['motes'] >= 250):
            itemOver250 = True
            break

if key_items_dict['shards'] >= 250:
    print(f"Shadowmourne obtained!")
    key_items_dict['shards'] -= 250
elif key_items_dict['fragments'] >= 250:
    print(f"Valanyr obtained!")
    key_items_dict['fragments'] -= 250
elif key_items_dict['motes'] >= 250:
    print(f"Dragonwrath obtained!")
    key_items_dict['motes'] -= 250

for item in key_items_dict:
    print(f"{item}: {key_items_dict[item]}")

for item in junk_items_dict:
    print(f"{item}: {junk_items_dict[item]}")