def calculate_price(item, item_quantity):

    cost = 0

    if item == "coffee":
        cost = 1.50
    elif item == "coke":
        cost = 1.40
    elif item == "water":
        cost = 1.00
    elif item == "snacks":
        cost = 2.00

    return cost * item_quantity

product = input()
quantity = int(input())

print(f"{calculate_price(product, quantity):.2f}")