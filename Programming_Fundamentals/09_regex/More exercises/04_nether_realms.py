import re

demons = [demon.strip() for demon in input().split(',')]
demons_dict = {}

for demon in demons:
    demons_dict[demon] = demons_dict.get(demon, {'hp': 0, 'dmg': 0})

health_pattern = r'[^0-9\+\-\*\/\.\s,]'
dmg_pattern = r'-?[0-9]+\.?\d*'
multipliers_pattern = r'[*\/]'

for demon in demons:
    health = 0
    damage = 0

    health_match = re.findall(health_pattern, demon)
    dmg_match = re.findall(dmg_pattern, demon)
    multi_match = re.findall(multipliers_pattern, demon)

    for char in health_match:
        health += ord(char)

    for digit in dmg_match:
        damage += float(digit)

    if multi_match:
        for char in multi_match:
            if char == '*':
                damage *= 2
            else:
                damage /= 2

    demons_dict[demon]['hp'] += health
    demons_dict[demon]['dmg'] += damage

for key, value in sorted(demons_dict.items(), key=lambda item: item):
    print(f"{key} - {value['hp']} health, {value['dmg']:.2f} damage")