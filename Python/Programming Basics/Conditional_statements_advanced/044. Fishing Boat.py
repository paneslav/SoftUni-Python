budget = int(input())
season = input()
people = int(input())

boatPrice = 0

if season == "Spring":
    boatPrice = 3000
elif season == "Winter":
    boatPrice = 2600
else:
    boatPrice = 4200

if people <= 6:
    boatPrice *= 0.9
elif 7 <= people <= 11:
    boatPrice *= 0.85
elif people >= 12:
    boatPrice *= 0.75

if people % 2 == 0 and season != "Autumn":
    boatPrice *= 0.95

if budget >= boatPrice:
    print(f"Yes! You have {abs(budget-boatPrice):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget-boatPrice):.2f} leva.")
    