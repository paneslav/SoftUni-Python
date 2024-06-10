to_do_list = input().split("|")
to_buy_list = []
energy = 100
coins = 100

isClosed = False

energy_to_gain = 0
coins_to_gain = 0
product_cost = 0
current_ingredient = ''

for element in to_do_list:

    if element[0:4] == "rest":  # rest
        energy_to_gain = int(element[5:])
        if energy < 100:
            if energy + energy_to_gain > 100:
                print(f"You gained {abs(((energy+energy_to_gain)-100) - energy_to_gain)} energy.")
                energy = 100
            else:
                energy += energy_to_gain
                print(f"You gained {energy_to_gain} energy.")
        elif energy == 100:
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")

    elif element[0:5] == "order":
        if energy >= 30:
            energy -= 30
            coins_to_gain = int(element[6:])
            coins += coins_to_gain
            print(f"You earned {coins_to_gain} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        to_buy_list = element.split('-')
        product_cost = int(to_buy_list[1])
        current_ingredient = to_buy_list[0]
        if coins >= product_cost:
            coins -= product_cost
            print(f"You bought {current_ingredient}.")
        else:
            print(f"Closed! Cannot afford {current_ingredient}.")
            isClosed = True
            break

if not isClosed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
