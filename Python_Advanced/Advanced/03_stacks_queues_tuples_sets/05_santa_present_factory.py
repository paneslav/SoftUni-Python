from collections import deque

requirements = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

toys_crafted = {}

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presentsCrafted = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    if current_material == 0 and current_magic == 0:
        continue

    if current_material == 0:
        magic.appendleft(current_magic)
        continue

    if current_magic == 0:
        materials.append(current_material)
        continue

    result = current_magic * current_material

    if result in requirements:
        toy = requirements[result]

        toys_crafted[toy] = toys_crafted.get(toy, 0)
        toys_crafted[toy] += 1
    elif result < 0:
        result = current_magic + current_material
        materials.append(result)
    elif result > 0:
        materials.append(current_material + 15)

if ('Doll' in toys_crafted and 'Wooden train' in toys_crafted) or \
        ('Teddy bear' in toys_crafted and 'Bicycle' in toys_crafted):
    presentsCrafted = True

if presentsCrafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")


if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(toys_crafted.items()):
    print(f"{key}: {value}")