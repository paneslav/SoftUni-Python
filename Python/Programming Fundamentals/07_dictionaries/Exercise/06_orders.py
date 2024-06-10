products_info = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break

    item = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if item not in products_info:
        products_info[item] = [price, quantity]
    else:
        products_info[item][1] += quantity
        if products_info[item][0] != price:
            products_info[item][0] = price

for item in products_info:
    print(f"{item} -> {products_info[item][0] * products_info[item][1]:.2f}")
