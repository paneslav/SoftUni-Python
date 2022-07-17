inventory = {}

while True:
    command = input()
    if command == "statistics":
        break

    key, value = command.split(': ')
    if key not in inventory.keys():
        inventory[key] = int(value)
    else:
        inventory[key] += int(value)

list_of_inventory = [f"- {item}: {inventory[item]}" for item in inventory.keys()]
products_to_print = "\n".join(list_of_inventory)

print("Products in stock:")
print(products_to_print)
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")