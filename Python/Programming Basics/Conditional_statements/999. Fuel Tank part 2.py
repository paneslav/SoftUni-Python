fuelType = input()
fuelQuan = float(input())
club = input()

cost = 0

if club == "Yes":
    if fuelType == "Gasoline":
        cost = fuelQuan * 2.04
    elif fuelType == "Diesel":
        cost = fuelQuan * 2.21
    elif fuelType == "Gas":
        cost = fuelQuan * 0.85
else:
    if fuelType == "Gasoline":
        cost = fuelQuan * 2.22
    elif fuelType == "Diesel":
        cost = fuelQuan * 2.33
    elif fuelType == "Gas":
        cost = fuelQuan * 0.93

if 20 <= fuelQuan <= 25:
    cost *= 0.92
elif fuelQuan > 25:
    cost *= 0.9

print(f"{cost:.2f} lv.")

