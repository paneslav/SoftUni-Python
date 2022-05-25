budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25

loaf_counter = 0
egg_counter = 0

loaf_cost = flour_price + egg_price + milk_price

while budget > 0 and budget >= loaf_cost:

    budget -= loaf_cost
    loaf_counter += 1
    egg_counter += 3

    if loaf_counter % 3 == 0:

        egg_counter -= loaf_counter - 2


print(f"You made {loaf_counter} loaves of Easter bread! Now you have {egg_counter} eggs and {budget:.2f}BGN left.")