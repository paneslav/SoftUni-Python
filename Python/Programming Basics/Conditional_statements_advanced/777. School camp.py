season = input()
groupType = input()
scholarsCount = int(input())
daysCount = int(input())

nightPrice = 0
sport = ""

if groupType == "mixed":
    if season == "Winter":
        nightPrice = 10
    elif season == "Spring":
        nightPrice = 9.50
    else:
        nightPrice = 20
else:
    if season == "Winter":
        nightPrice = 9.60
    elif season == "Spring":
        nightPrice = 7.20
    else:
        nightPrice = 15

totalCost = (daysCount*nightPrice) * scholarsCount

if scholarsCount >= 50:
    totalCost *= 0.5
if 20 <= scholarsCount < 50:
    totalCost *= 0.85
if 10 <= scholarsCount < 20:
    totalCost *= 0.95

if groupType == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    else:
        sport = "Volleyball"
elif groupType == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    else:
        sport = "Football"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    else:
        sport = "Swimming"

print(f"{sport} {totalCost:.2f} lv.")