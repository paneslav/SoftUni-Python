fuelType = input()
litresLeft = float(input())

if fuelType == "Diesel":
    if litresLeft >= 25:
        print(f"You have enough {fuelType.lower()}.")
    else:
        print(f"Fill your tank with {fuelType.lower()}!")
elif fuelType == "Gasoline":
    if litresLeft >= 25:
        print(f"You have enough {fuelType.lower()}.")
    else:
        print(f"Fill your tank with {fuelType.lower()}!")
elif fuelType == "Gas":
    if litresLeft >= 25:
        print(f"You have enough {fuelType.lower()}.")
    else:
        print(f"Fill your tank with {fuelType.lower()}!")
else:
    print("Invalid fuel!")