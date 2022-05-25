orders = int(input())

price_for_the_day = 0
total_money = 0

for _ in range(orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not (0.01 <= price_per_capsule <= 100.00) or not (1 <= days <= 31) or not (1 <= capsules_per_day <= 2000):
        continue

    price_for_the_day = (capsules_per_day * days) * price_per_capsule
    total_money += price_for_the_day
    print(f"The price for the coffee is: ${price_for_the_day:.2f}")

    price_for_the_day = 0

print(f"Total: ${total_money:.2f}")