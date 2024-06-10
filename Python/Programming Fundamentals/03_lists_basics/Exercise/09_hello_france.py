items_to_purchase = input().split("|")
budget = float(input())

item_price = 0
total_profit = 0
current_profit_price = 0

total_money = 0

for item in items_to_purchase:

    if item[0] == "C":
        item_price = float(item[9:])
        if item_price <= 50 and budget >= item_price:
            budget -= item_price
            current_profit_price = item_price * 0.4
            total_profit += current_profit_price
            total_money += current_profit_price + item_price
            print(f"{current_profit_price + item_price:.2f}", end=' ')

    elif item[0] == "S":
        item_price = float(item[7:])
        if item_price <= 35 and budget >= item_price:
            budget -= item_price
            current_profit_price = item_price * 0.4
            total_profit += current_profit_price
            total_money += current_profit_price + item_price
            print(f"{current_profit_price + item_price:.2f}", end=' ')

    else:
        item_price = float(item[13:])
        if item_price <= 35 and budget >= item_price:
            budget -= item_price
            current_profit_price = item_price * 0.4
            total_profit += current_profit_price
            total_money += current_profit_price + item_price
            print(f"{current_profit_price + item_price:.2f}", end=' ')

print()
total_money += budget

print(f"Profit: {total_profit:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")