budget = float(input())
season = input()

carType = ""
economicsClass = ""
carPrice = 0

if season == "Summer":
    carType = "Cabrio"
    if budget <= 100:
        economicsClass = "Economy class"
        carPrice = budget * 0.35
    elif 100 < budget <= 500:
        economicsClass = "Compact class"
        carPrice = budget * 0.45
    else:
        economicsClass = "Luxury class"
        carPrice = budget * 0.9
        carType = "Jeep"
else:
    carType = "Jeep"
    if budget <= 100:
        economicsClass = "Economy class"
        carPrice = budget * 0.65
    elif 100 < budget <= 500:
        economicsClass = "Compact class"
        carPrice = budget * 0.8
    else:
        economicsClass = "Luxury class"
        carPrice = budget * 0.9

print(f"{economicsClass}\n{carType} - {carPrice:.2f}")