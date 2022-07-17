products = input().split()
products_to_search = input().split()

stock = {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}

for product in products_to_search:
    if product not in stock.keys():
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {stock[product]} of {product} left")