from restaurant.restaurant import Restaurant

rest = Restaurant()

while True:
    try:
        command = input()

        if "изход" in command:
            print(rest.show_stats())
            break

        if "продажби" in command:
            print(rest.show_stats())
            continue

        if "инфо" in command:
            product_name = command.split(" ", 1)[1]
            product = rest.find_product_by_name(product_name)
            print(product)
            continue

        command = command.split(", ")

        # add products to menu
        if command[0][0].isalpha():
            rest.add_product_to_menu(*command)

        # make orders for table
        if command[0][0].isnumeric():
            rest.make_order(*command)

    except Exception as ex:
        print(str(ex))
