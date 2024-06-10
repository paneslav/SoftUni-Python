budget = float(input())
season = input()

placeType = ""
placePrice = 0
location = ""

if season == "Summer":
    location = "Alaska"
    if budget <= 1000:
        placePrice = budget * 0.65
        placeType = "Camp"
    elif 1000 < budget <= 3000:
        placePrice = budget * 0.8
        placeType = "Hut"
    else:
        placePrice = budget * 0.9
        placeType = "Hotel"
else:
    location = "Morocco"
    if budget <= 1000:
        placePrice = budget * 0.45
        placeType = "Camp"
    elif 1000 < budget <= 3000:
        placePrice = budget * 0.6
        placeType = "Hut"
    else:
        placePrice = budget * 0.9
        placeType = "Hotel"

print(f"{location} - {placeType} - {placePrice:.2f}")